<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1007.txt",
      "sha256": "4ae66d67d56bd70a24a52f55e70146113ae75cc5c975477ada9e827a445c14f3",
      "bytes": 13317
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "542fada6532248b4b2e6ff22e0a13686bc529bac7e971a9ac6f7ef275ce26aa1",
      "bytes": 1243
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a2ba2080787f93b9df4a81c1f6c7b6f602a1beff6efab59540e4d4c1fd5ee248",
      "bytes": 237214
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0e961ac1a0d7228c8c80b158c76358cc04518c1af5affe38a682e3b0621e0d7d",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a15c37386bc2b7fa2499b580ef826f96039f1af79a8a3ec1275c98c40844e7ca",
      "bytes": 1408
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "98429df2636d0111771f92927d01efd32317c133baf36b04bcea006bdda5d250",
      "bytes": 733
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "067729a2c21d0cebd6add3028ac0a1a91cfffc88528277258b279acb6a4401bb",
      "bytes": 275591
    }
  ],
  "estimated_tokens": 9486
}
-->

# Durable State Update — Chapter 1007

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1007. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1007. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 1007,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1007,
    "continuity_sources": [1007],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Gansu Murim has assembled 30,000 martial artists and arranged three defensive lines across Dunhuang, the Great Snow Mountain, and the Qilian Mountains; the Kongtong Sect is deployed.",
    "The Gansu force includes dark-path figures; Sima Gong has pledged his life to keep them in check, and Jeok Cheongang and Zhongnan elders support accepting them as allies against Dark Heaven.",
    "Sima Gong sent trusted scouts beyond the desert after ominous signs; their findings are unknown. He expects Dark Heaven to target Gansu and urges Jeok Cheongang to go to Qinghai.",
    "An urgent messenger has called to the Sect Leader from outside the meeting room; the message is unknown.",
    "Taishan remains unusually motionless and uneating at the feast; Namho reacted to a scent that recalled a recent memory."
  ],
  "continuity_sources": [
    1005,
    1006
  ],
  "open_questions": [
    "What did the scouts find beyond the desert, and what ominous signs prompted their mission?",
    "What is the urgent message from the messenger outside the meeting room?",
    "Why has Taishan stopped eating, and what caught Namho’s attention?"
  ],
  "safe_through": 1006,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 주화입마   | **qi deviation**                                 |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 감숙     | **Gansu**              |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 사검 | **Snake Sword** | Crooked-bladed weapon resembling a snake. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 황하 | **Yellow River** | River along which civilization began. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1005
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1006
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1006
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating, yet outwardly gentle; he uses persuasive sophistry and a calming manner to justify hard choices.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1007화



감숙성에서 나고 자란 이에게 있어, 사시사철 휘몰아치는 희뿌연 모래폭풍은 결코 드문 일이 아니었다.

아득한 과거, 일대를 기점으로 흐르던 물줄기가 황하(黃河)라 불리게 된 그때부터 이미 그들의 조상은 황토빛 고원(高原)이 있었음을 기록했으니까.

정확한 시기도, 생겨난 이유도 몰랐지만 황토 고원은 여전히 그곳에 있었다.

어디선가 거센 바람이 불어오는 날이면 용오름이 솟구치듯 한바탕 주위를 휩쓸었다가, 이내 미세하고 고운 황토를 별처럼 흩뿌리며 사라지곤 했다.

아마도 그래서였을 것이다.

성벽 위에서 번을 서고 있던 흑룡마문의 무인들이, 저 멀리 북쪽에서 다가오는 먼지구름을 보면서도 별다른 감흥을 느끼지 못했던 것은.

“염병할. 또 지랄이네.”

무인 중 한 명이 미간을 찌푸리자, 조장을 맡은 중년인이 익숙한 손놀림으로 품에서 천 쪼가리를 꺼냈다.

“주둥이 닥치고 복면이나 써. 지난번처럼 괜히 버티고 있다가 며칠 내내 투덜거리지 말고.”

“아니, 그때는 진짜 어쩔 수 없었다니까요. 갑자기 확 들이닥치는 걸 어떻게 피합니까? 그냥 숨이 턱 막히는데.”

“네놈 마음대로 해라. 또 밥 대신 모래나 한 움큼 처먹고 싶으면.”

곳곳에서 낄낄거리는 웃음소리가 흘러나오던 그때, 먼지구름을 주시하고 있던 누군가가 입을 열었다.

“그래도 뭐, 지금 오는 건 자그마하니 귀엽구먼. 보아하니 여기까지 닿기도 전에 알아서 사그라들겠는데? 멀찍이 앞에 나가 있는 척후조 놈들이야 옴팡 뒤집어쓰겠지만.”

“어, 맞네? 조장님, 복면 왜 쓰셨습니까?”

하루 이틀 겪는 일이 아니다 보니, 이제는 척하면 척이다.

십여 장이 넘게 솟구친 모래폭풍도 아니고, 자그마한 먼지구름에 수선을 떨 필요야 있나.

무인들은 눈으로 확인해 보지도 않은 채, 일찌감치 복면부터 뒤집어쓴 조장을 짓궂게 놀려 댔다.

“이거, 이거. 벌써 감 다 죽으셨네.”

“혈사검(血死劍)이라는 별호가 울겠소. 큭큭.”

“어허. 대충 봐도 견적 나오는데 뭘 그리 성급하셨습니까. 제가 소싯적에 마적 생활 좀 해 봐서 아는데, 한 서른 기 정도가 말머리를 나란히 한 채 달리면 딱 저 정도 크기가 나옵디다. 별거 아니에요.”

그 순간, 그렇지 않아도 험상궂기 그지없는 조장의 얼굴이 흉신악살처럼 일그러졌다.

“뭐?”

동시에 서서히 잦아드는 웃음소리.

한때 인근에서 제법 악명을 떨쳤다는 조장의 과거를 기억해낸 수하들이 마른침을 꿀꺽 삼켰다.

“그, 저희가 드리고 싶었던 말씀은 그게 아니옵고…….”

그러나 곧이어 들려온 조장의 한 마디에, 촉각을 곤두세우고 있던 수하들은 얼떨떨한 표정들이 될 수밖에 없었다.

“아니, 그거 말고.”

“예?”

“마지막에 말했던 놈. 뭐라고 했어?”

모두의 시선이 한 방향을 향해 쏠리자, 마적 생활을 했던 무인이 눈을 끔뻑였다.

“저 말입니까요?”

“그래. 아까 했던 말, 다시 해 봐.”

“그게 그러니까, 어허, 대충 봐도 견적 나오는 게 뭘 그리 성급…….”

“그거 말고, 이 개자식아! 그 다음에!”

“저, 저 정도 크기의 먼지구름이면 기마병 서른 기 정도…….”

“그럼 반 시진 전에 출발했던 척후조 숫자는?”

“정확히 서른입니다. 아까 말 내어줄 때였나. 해 떨어질 때까지 순찰해야 되니까 더 괜찮은 놈들로 달라고 개지랄을 떨어서 똑똑히 기억하고 있…….”

미처 이어지지 못하고 뚝 끊기는 목소리.

그제야 뭔가 이상함을 알아차린 무인들은 눈동자를 뒤룩뒤룩 굴리며 서로를 향해 들리지 않는 대화를 주고받았다.

‘잠깐. 뭐지 이거?’

‘평소보다도 훨씬 작은 먼지구름. 기마병 서른 기. 마지막으로 척후조 서른.’

‘쎄한데.’

‘해 떨어지고 나서야 돌아올 놈들이 왜 벌써 돌아와?’

‘더 쎄한데.’

‘혹시 용변이 급했나?’

‘아무 데나 싸고 덮으면 그게 측간이지, 용변 보려고 임무까지 내팽개치고 돌아오는 미친놈이 있을 리가.’

‘다들 그렇지 않나? 난 그런 편인데.’

‘진짜 미친놈인가.’

‘이거 진짜 엄청나게 쎄한데.’

아무리 머리를 맞대고 생각해도, 모든 상상력을 총동원해도 심상치 않은 상황.

꿀꺽.

묘한 긴장감 속, 누군가가 마른침을 삼킨 그 순간이었다.

쐐애애액, 펑!

수백여 장 밖, 희뿌연 먼지구름 사이로 솟구쳐오르는 적색 연기. 척후조에게 주어진 그 신호용 폭죽에 담긴 의미를 알아차린 조장이 목소리를 쥐어 짜냈다.

“거수자 발견……!”

거수자란 거동이 수상한 자, 즉 낯선 침입자를 의미하는 바.

이내 현실을 깨달은 성벽 위의 무인들이 피를 토하듯 부르짖었다.

“실제 상황! 실제 상황이다!”

“뭐 해! 개자식들아! 빨리빨리 안 움직이고!

“무, 문주님께 알려라! 어서!”

마치 화약고가 터진 것처럼 어수선해진 성벽 위의 상황과 달리, 허공에서 화려하게 폭발한 폭죽은 먼지구름을 일으키며 죽을 힘을 다해 달려오는 서른 기의 척후조의 머리 위로 천천히 떨어져 내렸다.

그리고 굽이 굽이진 수십여 개의 언덕 중 한 곳에서, 그림자를 등진 채 그 광경을 지켜보는 일단의 무리가 있었다.

“이거…… 아주 난리가 났구만.”

정체를 알 수 없는 오십여 명의 기마인.

그중 선두에 선 거한(巨漢)의 침음성에, 말머리를 나란히 한 채 서 있던 또 다른 사내가 덥수룩하게 자라난 머리카락을 벅벅 긁었다.

“하, 씨. 미치겠네. 그러게 소제(小弟)가 천천히, 사근사근하게 접근하자고 하지 않았습니까.”

거한이 눈살을 찌푸리며 대답했다.

“괜히 질겁해서 도망칠 줄은 몰랐지. 혹시 몰라서 백기(白旗)까지 준비했는데. 저 새끼들 왜 저리 겁이 많아?”

“몰라서 묻습니까? 대형(大兄) 얼굴을 좀 보십쇼. 그런 인상으로 백기를 내밀어 봤자 좋은 뜻으로 받아들일 수 있는지.”

누군가의 핀잔에, 사방에서 격한 동의가 빗발쳤다.

“그게 맞지. 상판부터가 아주 흉악한데 백기가 뭔 소용이여.”

“곧 뒈질 네놈들한테 미리 조의를 표한다. 뭐 그런 뜻으로 받아들였을 것 같습니다.”

“백기가 아니라 백의를 입고 갔어도 안 돼.”

“그러면 곧 뒈질 네놈들에게 조의를 표하기 위해 상복까지 미리 갖춰 입었다. 뭐 그 뜻이죠.”

“말이 필요 없지. 흉악하게 생겨 먹은 것만 따지면 천마 할애비도 대형은 못 이겨.”

“염병. 상황이 개판으로 돌아가니까 슬슬 후달리네. 이거 괜히 다가갔다가 화살비부터 쏟아지는 거 아뇨?”

“어쩔 수 없지. 대형, 기왕 이렇게 된 거 차라리 지금이라도 돌아갑시다.”

“둘째 형님. 쫄았소?”

“갈! 쫄긴 누가! 중요한 걸 놓고 온 게 생각나서 그래!”

“보아하니 팍 쪼그라든 간덩이는 잘 챙겨 오셨고…… 아, 불알을 놓고 오셨구먼.”

“갈! 셋째, 네놈이 감히!”

“아니, 틈만 나면 자꾸 갈갈거려. 그런 것도 초절정 고수가 해야 멋있는 거요. 둘째 형님은 꿈도 못 꾼다니까.”

“갈! 네놈이 진정 관을 봐야 정신을 차리겠느냐!”

“자꾸 들으니까 미치겠네. 괜히 이상한 버릇 들어 가지고. 그래서 대형, 어쩌실 겁니까?”

셋째라 불린 사내의 물음에, 속사포처럼 쏟아지는 목소리 사이에서도 침묵을 지키던 거한이 비로소 입을 열었다.

“우린 돌아가지 않는다.”

덩치만큼이나 무거운 목소리. 거한은 착 가라앉은 눈빛으로 아지랑이 너머에 우뚝 선 황토빛 성벽을 응시했다.

“다들 무엇을 걱정하는지 내 모르는 바가 아니나…… 이건 대인(大人)께서 친히 부탁하신 것. 너희가 신의를 아는 사내들이라면 내 말을 따라 다오.”

“……!”

“……!”

준엄하기 그지없는 거한의 모습에, 그를 대형이라 부르던 여섯 사내의 눈동자가 파르르 떨렸다.

물론, 뒤이어 그들 사이에서 흘러나온 중얼거림은 거한이 기대했던 반응은 아니었다.

“분위기 잡는다, 또.”

“이렇게 되면 우리만 나쁜 새끼들이지.”

“이럴 때만 보면 곰이 아니라 순 여우라니까. 안 그렇소, 형님들?”

“그래도 다 같이 대형 말씀을 따르시지요. 더군다나 다른 사람도 아니고 대인께서 부탁하신 건데. 별수 있겠습니까.”

“갈……!”

“제발 부탁인데 누가 둘째 형님 입에 재갈 좀 물려라. 계속 듣고 있자니 주화입마 오겠다.”

대부분이 당과를 뺏긴 어린아이처럼 투덜거렸지만, 거한은 물론 그들의 뒤에서 모든 상황을 지켜보던 수십여 명의 기마인들도 알고 있었다.

비록 상황이 이리되었어도, 그들의 목적은 변하지 않는다는 것을.

또한 그 확신을 뒷받침하는 가장 큰 증거는, 자신들을 이곳으로 보낸 누군가의 존재였다.

“가자. 이러다가 해 저물겠다.”

이제야 서쪽에서부터 느지막히 번져오는 석양을 받으며, 거한을 필두로 한 오십여 명의 기마인은 언덕을 넘어 내달리기 시작했다.

그리고 머지않아 성벽에 도달한 그들을 기다리고 있던 것은, 빽빽하게 겨누어진 수백여 발의 화살촉과 그 사이로 보이는 낯선 얼굴들이었다.

“정지 정지 정지! 손들어! 움직이면 쏜다!”

기생 오래비처럼 생긴 웬 젊은 놈의 외침에, 거한은 침착하게 준비해두었던 백기를 품에서 꺼내 들었다.

아니, 정확히는 꺼내들려고 했다.

앞서 입을 연 그 젊은 놈이, 생각지도 못한 명령을 내리기 전까지는.

“발사!”

“……어?”



* * *



쉬쉬쉬쉬쉭!

수백여 발의 화살이 공기를 찢었다.

단지 힘의 차이가 있을 뿐, 크거나 작거나 일단 공력을 머금은 그것들은 곡선이 아닌 직선으로 내리꽂혔다.

때아닌 불청객들을 향해.

카카카카캉!

사방으로 불꽃이 비산했다.

수십여 명의 수하들을 뒤로하고 홀로 앞서 나와, 반경 삼십여 장을 빼곡히 뒤덮은 화망(火網)에서 살아남은 거한이 버럭 외쳤다.

“아니, 이런 미친 새끼를 봤나! 다짜고짜 활부터 쏘는 게 어디 있어!”

내 옆에 있던 적천강이 고개를 끄덕였다.

“더럽게 흉악하게 생긴 놈이지만, 저 말에는 노부도 동의할 수밖에 없군. 혹시 뭐 심마(心魔)에 사로잡히기라도 했느냐?”

“아뇨, 멀쩡한데요.”

“그럼 왜?”

“손들라고 했는데 말 안 들었잖아요. 이 새끼가 어딜 밑장빼기를 시도해.”

“미친놈이로고.”

“사실 진짜로 쏠 줄 몰랐습니다. 제 명령은 안 들을 줄 알았는데. 뭐, 대충 수준 보니까 이 정도는 살아남을 것 같아서 경고하는 의미로 한 것도 있고요. 여하튼 아무일 없으니 된 거 아닙니까?”

“무량수불…….”

내 명쾌한 결론에 풍운검군이 아연질색한 얼굴로 중얼거렸지만, 그와는 달리 흑야왕 사마공은 너털웃음을 터트렸다.

“하하. 아주 시원시원하군. 자네 같은 사람이 우리 쪽에 있었어야 했는데.”

“…….”

이거 칭찬이냐, 악담이냐.

내가 잠시 어떻게 반응해야 하나 고민하는 사이, 어떻게 저렇게 생길 수 있을까 싶을 정도로 흉악한 인상을 자랑하는 거한이 잇따라 외쳤다.

“쏘지 마! 쏘지 말란 말이다! 내 손에 들린 이것이 안 보이는가!”

펄럭.

뭘 하려고 품에 손을 넣었나 했더니, 거한이 힘차게 휘두르는 것은 커다란 천이었다.

모래 먼지와 황토로 범벅이 된, 애매하기 짝이 없는 누리끼리한 천.

“저게 대관절 뭘 뜻하는 거요? 싯누런 거 들고 뭘 보라는 건지.”

“황색 천…… 헛, 설마 황건적(黃巾賊)?”

“그게 무슨 말도 안 되는. 시대가 어느 때인데 황건적이 아직도 남아 있단 말이오?”

의견이 분분한 사람들의 모습에, 나는 다시 한번 명쾌한 해답을 내놓아야 한다는 막중한 책임감을 느꼈다.

‘거동이 수상한데다가 흉악하게 생겨 먹은 놈. 거기에 더해 같이 온 놈들도 최소 전과 18범쯤 되어 보이는 인상이라.’

아무리 생각해도, 당장 떠오르는 해결책은 하나뿐이다.

“일제 사격 준비.”

“어……?”

“발사!”

쉬쉬쉬쉭!
```

## Final English reading copy

```markdown
# Chapter 1007

For someone born and raised in Gansu Province, the pale sandstorms that swept through in every season were nothing unusual.

Since time immemorial, from the days when the river that flowed through the region came to be called the Yellow River, their ancestors had recorded the existence of the loess-colored plateau.

No one knew exactly when it had formed or why, but the plateau was still there.

On days when a strong wind blew in from somewhere, it would sweep through the area like a waterspout, then vanish, scattering fine, soft loess like stars.

That was probably why.

The martial artists of the Black Dragon Demon Gate standing watch atop the city wall felt little as they watched a cloud of dust approach from the far north.

“Damn it. Here we go again.”

One of the martial artists frowned. The middle-aged man leading their squad pulled a scrap of cloth from inside his clothes with a practiced motion.

“Shut your mouth and put on your mask. Don’t stubbornly stand there like last time, then spend the next few days complaining.”

“No, I really couldn’t help it that time. How are you supposed to dodge when it hits you all at once? It takes your breath away.”

“Do whatever you want. If you’d rather eat a handful of sand than your next meal.”

Just then, as chuckles rippled through the group, someone watching the cloud of dust spoke up.

“Still, what’s coming now is small and cute. Looks like it’ll die down on its own before it even gets here. The scouts way out front are going to get buried, though.”

“Oh, you’re right. Captain, why’d you put on your mask?”

They’d dealt with this more times than they could count. By now, they knew the drill.

It wasn’t a sandstorm towering more than ten jang high. There was no need to make such a fuss over a little cloud of dust.

Without even bothering to check for themselves, the martial artists teased their Captain, who’d put on his mask early.

“Look at you, Captain. You’ve lost your touch.”

“The Blood-Death Sword title will be weeping. Heh.”

“Now, now. You can tell what it is at a glance. Why the rush? I used to be a mounted bandit when I was young, and I know a group of about thirty riders traveling side by side kicks up a cloud about that size. It’s nothing.”

In that instant, the Captain’s already fearsome face twisted into something monstrous.

“What?”

The laughter slowly died away.

His subordinates remembered that the Captain had once been fairly notorious in the area. They swallowed hard.

“W-we didn’t mean it like that, Captain……”

But at the Captain’s next words, the men who’d been on edge could only stare at him in confusion.

“No, not that.”

“Pardon?”

“The last thing that guy said. What was it?”

Everyone’s eyes turned toward the mounted bandit. He blinked.

“Me?”

“Yeah. Say what you said before again.”

“Uh, well, you can tell what it is at a glance, so why the rush—”

“Not that, you idiot! The next part!”

“Th-that a cloud of dust that size means about thirty mounted—”

“And how many scouts left half a shichen ago?”

“Exactly thirty. Was that when they got their horses earlier? I remember because they made a huge fuss, demanding better mounts since they had to patrol until sunset……”

His voice cut off before he could finish.

Only then did the martial artists realize something was wrong. Their eyes darted back and forth as they held an inaudible conversation among themselves.

*Wait. What’s going on?*

*An unusually small cloud of dust. Thirty mounted warriors. And, finally, thirty scouts.*

*Something feels off.*

*Why are they back already if they weren’t supposed to return until after sunset?*

*That feels even more off.*

*Maybe they had to take a dump?*

*You can shit anywhere, cover it up, and call it a latrine. What kind of lunatic would abandon a mission just to come back and relieve himself?*

*Isn’t that what everyone does? I do.*

*You’re a real lunatic.*

*This feels seriously wrong.*

No matter how hard they thought, no matter how much they wracked their brains, something was clearly amiss.

Gulp.

In the strange tension, just as someone swallowed dryly—

Fwoooosh! Boom!

Hundreds of jang away, red smoke shot up from the pale cloud of dust. The Captain recognized what the signal flare assigned to the scouts meant and forced his voice out.

“Suspicious persons spotted……!”

Suspicious persons meant people acting strangely—in other words, unfamiliar intruders.

At last realizing what was happening, the martial artists atop the wall shouted as if coughing up blood.

“Real situation! This is real!”

“What are you waiting for, you bastards? Move your asses!”

“L-let the Sect Leader know! Hurry!”

The wall erupted into chaos as if a powder magazine had exploded. Meanwhile, the flare that had burst brilliantly in the sky slowly drifted down over the thirty scouts racing toward them with all their might, raising a cloud of dust.

And on one of the dozens of hills, a group watched the scene with their backs to the shadows.

“Well…… this is a hell of a mess.”

About fifty mounted warriors of unknown identity stood there. At the front of the group, a giant let out a low groan. Beside him, another man scratched at his shaggy hair.

“Ah, damn it. This is driving me crazy. Didn’t your little brother tell you we should approach slowly and gently?”

The giant frowned.

“I didn’t think they’d panic and run. We even brought a white flag just in case. Why are those bastards so scared?”

“Do you really need to ask? Take a look at your own face, Big Brother. Do you think anyone’s going to take a white flag as a friendly gesture when you look like that?”

At someone’s chiding, agreement erupted from all around them.

“He’s right. Your face is downright terrifying. What good’s a white flag going to do?”

“They probably thought you were offering your condolences in advance to the poor bastards about to die.”

“It wouldn’t have helped if you’d gone over wearing white clothes instead of carrying a white flag.”

“Then they’d think you’d dressed in mourning ahead of time to offer your condolences to the poor bastards about to die.”

“Nothing to be done. Even the Heavenly Demon’s granddaddy couldn’t beat Big Brother when it comes to looking vicious.”

“Damn it. This whole situation’s going to shit, and now I’m starting to get nervous. What if we ride over there and they shower us with arrows?”

“Can’t be helped. Big Brother, since it’s come to this, let’s just turn around and go back.”

“Second Brother, are you scared?”

“Enough! Who’s scared? I just remembered I left something important behind!”

“Looks like you brought your shriveled-up guts along just fine…… Ah, you left your balls behind.”

“Enough! Third Brother, how dare you!”

“Honestly, you keep going on like that. It’s only cool when a Supreme Peak master does it. You can’t pull it off, Second Brother.”

“Enough! Do you have to see your own coffin before you learn your lesson?”

“I’m going to lose my mind if I have to keep listening to that. You’ve picked up a weird habit. So, Big Brother, what are you going to do?”

At the question from the man called Third Brother, the giant, who’d kept silent even as voices flew back and forth, finally spoke.

“We’re not turning back.”

His voice was as heavy as his build. With a steady gaze, the giant stared at the loess-colored wall standing tall beyond the shimmering heat.

“I know what you’re all worried about…… But this is a personal request from the Great One. If you’re men who understand loyalty, do as I say.”

“……!”

“……!”

At the giant’s stern words, the eyes of the six men who called him Big Brother trembled.

Of course, the mutters that followed weren’t the reaction the giant had hoped for.

“There he goes, putting on a show again.”

“Now we’re the bad guys.”

“He’s a bear in name only. He turns into a fox whenever it suits him. Am I right, brothers?”

“Still, we should all do as Big Brother says. Besides, this request came from the Great One himself. What choice do we have?”

“Enough……”

“Please, someone gag Second Brother. Listening to him is giving me qi deviation.”

Most of them grumbled like children who’d had their sweets taken away. But the giant—and the dozens of mounted warriors watching from behind him—knew the truth.

Even though things had turned out this way, their purpose hadn’t changed.

And the strongest proof of that conviction was the person who’d sent them here.

“Let’s go. The sun’s going to set at this rate.”

Bathed in the sunset spreading late from the west, the fifty or so mounted warriors set off over the hill, led by the giant.

Before long, they reached the wall. Waiting for them were hundreds of arrowheads trained on them, and unfamiliar faces visible between the shafts.

“Stop! Stop! Stop! Hands up! Move and we’ll shoot!”

At the shout from some young pretty boy, the giant calmly reached into his clothes to pull out the white flag he’d prepared.

Or rather, he tried to pull it out.

He didn’t get the chance—not before that young man issued a command he hadn’t expected.

“Fire!”

“……Huh?”

* * *

Fwoosh, fwoosh, fwoosh, fwoosh!

Hundreds of arrows tore through the air.

Their strength varied, but large or small, once they were imbued with internal energy, they plunged down in straight lines instead of arcs.

Straight at the unexpected visitors.

Clang-clang-clang-clang!

Sparks flew in all directions.

The giant stood ahead of his dozens of subordinates, alone. Having survived the net of arrows that had densely covered a thirty-jang radius, he bellowed.

“Are you out of your damn mind? Who starts shooting arrows without warning?”

Jeok Cheongang, standing beside me, nodded.

“He looks vicious as hell, but I can’t help agreeing with him. Have you been seized by a mind demon or something?”

“No, I’m fine.”

“Then why?”

“I told him to put his hands up, and he didn’t listen. That bastard tried to pull a fast one on me.”

“You’re insane.”

“Honestly, I didn’t think they’d really shoot. I thought they’d ignore my order. Judging by their level, though, I figured they’d survive a volley like that, so I did it as a warning. Anyway, no harm done, right?”

“Infinite Life Buddha……”

The Wind-and-Cloud Sword Lord muttered, looking appalled at my airtight conclusion. Unlike him, the Black Night King Sima Gong let out a hearty laugh.

“Haha! Straight to the point. We could’ve used someone like you on our side.”

“……”

Was that a compliment or an insult?

While I was trying to decide how to respond, the giant, whose face was so vicious it was hard to believe anyone could actually look that way, shouted again.

“Don’t shoot! I said don’t shoot! Can’t you see what I’m holding?”

*Flap.*

So that was what he’d reached into his clothes for. What the giant was waving around was a large piece of cloth.

A questionable shade of yellow, completely covered in sand and loess.

“What on earth is that supposed to mean? Why’s he waving around that dingy yellow thing?”

“Yellow cloth…… Wait, could he be a Yellow Turban?”

“That makes no sense. What era do you think this is? How could the Yellow Turbans still be around?”

At the sight of everyone debating, I felt the weighty responsibility of having to offer another clear-cut answer.

*A suspicious-looking guy with a vicious face. And the others with him look like they’ve each got at least eighteen prior convictions.*

No matter how I looked at it, there was only one solution that came to mind.

“Prepare a volley.”

“Uh……?”

“Fire!”

Fwoosh, fwoosh, fwoosh!
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1008.txt",
      "sha256": "1252803ac7cdbdb5e7b45a05f71183d89eb4c3fc974310b30af4130ba2240773",
      "bytes": 12896
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "cbb7cb3dd84af5bfe736eff771afde657ab28ee25139faa06e70b9f87d163b45",
      "bytes": 597
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a2ba2080787f93b9df4a81c1f6c7b6f602a1beff6efab59540e4d4c1fd5ee248",
      "bytes": 237214
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a54ab5d9aaeb4a013c6bb70d01239439fafaf98601bc586bcb2782a641560a14",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "fb60d7b1740880e617e3ef4f8c41f0aa08ac731600a187fd7d4bcff7d69978bd",
      "bytes": 1408
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "82b01b2fc275fee8eaad73dd06fa8cff0ea0afce8bdc292f40d6d662907e519d",
      "bytes": 733
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "067729a2c21d0cebd6add3028ac0a1a91cfffc88528277258b279acb6a4401bb",
      "bytes": 275591
    }
  ],
  "estimated_tokens": 9600
}
-->

# Durable State Update — Chapter 1008

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
1 and safe_through 1008. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1008. Profile updates may replace only one
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
  "chapter": 1008,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1008,
    "continuity_sources": [1008],
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
    "The thirty scouts returned early and signaled that suspicious intruders were approaching the Gansu wall.",
    "About fifty unidentified riders led by a giant arrived at the wall on a personal request from the Great One; their purpose and identity remain unknown.",
    "Jin Taekyung ordered the wall guards to fire on the riders, who survived the volleys."
  ],
  "continuity_sources": [
    1007
  ],
  "open_questions": [
    "Who are the riders, and what is the Great One’s request?"
  ],
  "safe_through": 1007,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 감숙     | **Gansu**              |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 도쿄핫 | **Tokyo Hot** | Adult-video studio referenced in Taekyung's insult; footnoted. |
| 피카소 | **Picasso** | Modern painter invoked in the comparison for Gung Gibang’s face. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 상주 | **chief mourner** | Funeral role assumed by Go Jun for Lee Jungryong. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |
| 포청천 | **Judge Bao** | Legendary magistrate invoked as a comparison for the Deputy Stronghold Lord. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 도쿄 | **Tokyo** | City visible behind Huginn's departing ship. |
| 진중 | **Jinzhong** | County included in Taekyung’s fief. |
| 녕하성 | **Ningxia Province** | Region between Gansu and Shaanxi. |

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

- **Safe through:** Chapter 1007
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1007
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1007
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating, yet outwardly gentle; he uses persuasive sophistry and a calming manner to justify hard choices.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1008화



결론만 말하자면, 세 차례의 화살비가 끝났을 때쯤 감숙 무림의 수뇌부들은 거한을 포함한 오십여 명의 괴한들을 기꺼이 성문 안으로 들이기로 결정했다.

물론 수뇌부 전체의 의견이라고 하기에는 어폐가 있었다.

이 결정에는 적천강의 존재가 매우 크게 작용했으니까.

“어디서 굴러먹다 온 개뼉다귀들인지는 모르겠으나, 우선은 살려서 들여보내라.”

그리고 웅성거리는 수뇌부를 향해 이렇게 덧붙였다.

“뭘 그리 고민하고 자빠졌느냐. 영 수상쩍다 싶으면 죽여서 내보내면 되는 것을.”

“오.”

“아.”

포청천도 개작두를 탁 칠 정도로 명쾌한 해답에 회의 같지도 않은 회의는 막을 내렸고, 흑야왕 사마공은 즉각 자신의 수하들에게 저 흉악한 생김새의 불청객들을 받아들이라 지시했다.

구구구궁.

조금씩 열리기 시작하는 육중한 철문.

그 틈새로 가장 먼저 발걸음을 내디딘 거한이 희번덕거리는 눈으로 주위를 둘러보았다.

무려 세 번에 달하는 화살비를 피하느라 피똥을 싼 그는 거의 넝마 차림이 되어 있었고, 반쯤 뒤집힌 눈동자는 누군가를 찾기 위해 분주하게 움직이고 있었다.

이를테면, 난데없이 발사 명령을 내린 어느 젊은 놈이라든지.

“혹시 누구 찾는 사람 있어? 계속 그러다가 목에 담 걸릴 것 같은데, 내가 대신 찾아줄까?”

때아닌 불청객들을 맞이하기 위해 가장 먼저 내려온 내가 불쑥 한마디를 던지며 나서자, 거한이 눈을 부릅떴다.

“너, 너……!”

“위에서 다 봤어. 잘 막고, 잘 피하더라.”

“이 기생 오래비 같은 놈이 감히!”

“너, 지금 뭐라고 했어?”

일순간 표정을 굳힌 내게서 흘러나오는 범상치 않은 기도에, 본능적으로 흠칫한 거한이 다시 한번 목소리를 쥐어 짜냈다.

“기생 오래비 같이 생긴 놈……!”

“잠깐. 잠깐만 기다려 봐.”

“뭐?”

분노와 의문이 뒤섞인 거한의 반문을 뒤로한 채, 나는 지그시 눈을 감았다.

‘기생 오래비같이 생긴 놈이라니.’

이 얼마나 듣기 좋은 말인가.

같은 염색체를 동일성별의 남성에게 이런 말을 듣는다는 건 실로 엄청난 극찬.

나는 파도처럼 밀려오는 감동의 여운을 갈무리하며 눈을 떴다.

“고맙다. 알고 보니 착한 놈이었구나, 너.”

“……?”

“그래서, 우리 중걸이는 어디에서 왔니?”

“……!”

거한, 아니 마중걸의 눈이 툭 튀어나왔다.

“그걸 어떻게!”

“응? 뭐를?”

“내, 내 이름.”

이제는 말까지 더듬는 그의 모습에, 나는 천연덕스럽게 대꾸했다.

“말했잖아. 아까 통명성까지 해 놓고 벌써 잊었어?”

“내가……?”

“아직 정신이 없나 보네. 그럴 만하지. 그 많은 화살을 다 피해야 했으니.”

아마 마중걸은 앞으로도 영원히 알 수 없을 것이다.

지금 이 순간, 자신의 머리 위에 반투명한 홀로그램 창이 유령처럼 둥둥 떠다니고 있다는 것을.



[Lv.80 마중걸]



80레벨.

저마다의 레벨이 그 사람이 지닌 무력의 절대적인 척도는 아니지만, 그렇다 하더라도 암천의 끄나풀이라고 생각하기에는 너무나도 소소한 수준이다.

‘아까 보인 모습만 봐도, 조금 완숙한 경지에 다다른 절정 고수 정도?’

그러나 의심의 끈을 이렇게 쉽게 놓아서는 안 되는 법.

여전히 귀신에 홀린 듯한 표정을 짓고 있는 마중걸을 천천히 훑어보던 그때, 적천강을 포함한 성벽 위의 수뇌부들이 드디어 계단을 통해 모습을 드러냈다.

그리고 때마침 오십여 인의 기마인들 역시 앞다투어 달려오는 중이었다.

“멈추시오!”

“말로, 말로 합시다!”

“우리는 싸울 의사가 없습니다!”

“아이고, 대형! 괜찮으십니까!”

“갈!”

“미치겠네, 진짜. 그거 그만 좀 하라니까.”

오십여 인의 기마인. 그중에서도 가장 선두에서 나란히 달려온 여섯 명의 사내가 마중걸을 에워쌌다.

‘뭐지, 이것들은.’

모르긴 몰라도, 이 자리의 모두가 나와 비슷한 생각을 떠올렸음이 분명했다.

길쭉이. 난쟁이. 주먹코. 뱁새눈…….

저마다 상당한 특색과 자유로운 이목구비를 자랑하는 그들은 결코 쉽게 볼 수 없는 조합이었고, 그 여섯 사내의 중심에 선 마중걸의 존재는 화룡점정(畵龍點睛)이나 다름없었다.

‘혹시 아버지가 피카소인가?’

다들 어느 정도의 인상파였는지, 나름 밑바닥 생활을 거쳤다는 흑룡마문의 무인들조차 본능적으로 검파(劍把)에 손을 가져갈 정도.

스릉.

그리고 곳곳에서 흘러나오는 미세한 마찰음이 긴장감을 고조시키던 그때, 나직한 음성이 모두의 귓가를 파고들었다.

“장담컨대, 지금부터 헛짓거리하는 놈들은 노부와 아주 뜨거운 시간을 보내게 될 것이다.”

목소리의 주인을 모르는 이는 이 자리에 아무도 없다.

더불어 당연하게도, 천하의 도쿄핫도 명함을 내밀 수 없는 JCK-444 불쇼 특집 영상에 참여하고 싶은 이들도 없었다.

처처척.

마치 화마(火魔)를 피하듯 좌우로 갈라지는 인의 파도.

그 너머로 수뇌부들을 이끌며 나타난 적천강은 마중걸을 흘끗 바라보더니, 이내 나를 향해 고개를 돌렸다.

“그래서, 어디에서 온 누구라고?”

“이름은 마중걸이고, 어디에서 왔는지는 아직 모릅니다.”

“암천의 끄나풀일 가능성은?”

“일단 조져 봐야 확실해지겠죠. 다만 이미 아시다시피 딱히 뭔가 수작을 벌일 만한 느낌도, 수준도 아니라서…….”

“단지 느낌으로 판단할 수 없는 일이다. 저것들이 의도적으로 무위를 감추었을 가능성에 대해서는 어찌 생각하느냐?”

적천강이 몰라서 묻는 것이 아니다. 우리의 대화에 귀를 기울이고 있는 모두에게 들으라고 던진 질문이었고, 그 의도를 깨달은 나는 망설임 없이 대답했다.

“없습니다.”

“그렇게 생각하는 근거가 있을 터.”

“노, 아니 스승님과 여기 계신 다른 분들을 속일 정도로 무위가 고강하다면 최소 반박귀진(返朴歸眞)이나 환골탈태(換骨奪胎)를 거쳐야 하죠.”

“그런데?”

“저 흉악하기 짝이 없는 면상들을 보십시오. 그 정도의 경지까지 다다른 초절정 고수라면 저따위로 생겨 먹을 수가 없습니다.”

“……!”

“……!”

마중걸을 포함한 일곱 흉신악살, 아니 사내들이 신형을 부르르 떨었지만 뭐 어쩌겠나. 그게 사실인데.

졸지에 변호사 노릇을 하게 된 나는, 알 수 없는 사명감을 느끼며 말을 이었다.

“하여, 저는 ‘흉신악살들이 무공을 숨김’ 건에 대하여 혐의없음으로 판단하고 변론을 마치겠습니다.”

적천강이 경탄 어린 표정으로 고개를 끄덕였다.

“네 녀석의 말이 실로 논리정연하여, 노부로서도 도무지 반박할 엄두가 나지 않는구나.”

“감사합니다.”

“하지만 저 황건적인지 암천인지, 그도 아니면 최소 마교에서 한 자리씩 해 처먹었을 것 같은 상판들을 보아하니 여간 수상쩍은 게 아니다.”

“그럼 뭐, 어쩌시려고요?”

“저것들이 지금 당장 모든 사실을 실토하거나, 아니면 화염신장으로 족칠 것이다.”

목소리는 나를 향하고 있지만, 눈빛은 아니다.

화염이 줄기줄기 쏟아지는 것 같은 적천강의 시선을 받은 마중걸이 하얗게 질린 얼굴로 더듬더듬 입을 열었다.

“호, 혹시 진짜 화왕 적천강 대협…….”

적천강이 심드렁한 얼굴로 대꾸했다.

“그럼 진짜지, 가짜겠느냐?”

“그렇다는 건 저 기생 오래비, 아니 젊은 분께서는 열화신룡…….”

이번엔 내가 나설 차례다.

다시금 듣게 된 기분 좋은 표현에 진한 미소를 머금은 나는 겁에 질린 마중걸을 다독였다.

“기생 오래비라고 계속 불러요. 편하게. 생각해 보니까 지금까지 반말한 것도 내가 예의가 없었네. 미안해요. 응?”

“아, 아닙니다. 그보다 아까부터 오해가 있으신 모양인데 해명 삼아 한 말씀 올려도 되겠습니까?”

“이제야 말이 좀 통하네. 그러게 진작 말씀을 말씀하시지.”

“아니, 말씀드리려고 했는데 다짜고짜…….”

“아, 말씀하시라고. 서두 떼고.”

내 부드러운 윽박지름에 주춤거리며 어깨를 편 마중걸이, 적천강을 포함한 수뇌부들을 향해 조심스럽게 입을 열었다.

“거두절미하고 말씀드리자면, 저희는 녕하 땅에서 왔습니다.”

“잠깐. 녕하라면 혹시…….”

문득 뇌리를 스치는 생각에 눈살을 찌푸린 순간, 마중걸이 황급히 덧붙였다.

“마적이 아닙니다!”

적천강이 중얼거렸다.

“어째 면상들이 심상치 않다 싶더니만, 녕하성에 똥물을 흩뿌리고 다닌다는 바로 그 마적 놈들이었구먼.”

“하, 한때 잠시 마적단에 몸담았던 것은 사실이나 지금은 결코…….”

그때, 풍운검군이 불쑥 끼어들었다.

가자미 눈으로 마중걸과 그 수하들을 훑으면서.

“무량수불. 도를 추구하는 자로서 할 말은 아니지만, 적 대협께서 말씀하셨듯이 저 얼굴은 현업이 분명합니다.”

그 말에 동의하듯 여기저기서 고개가 끄덕여졌다.

그리고 마치 현대 사회에서 외모지상주의가 판치는 이유를 입증하듯, 서서히 험악해지는 분위기 속에서 한 사람의 입술이 열렸다.

“마중걸, 마중걸…… 혹, 그대가 백마방(白馬房)의 바로 그 마중걸인가?”

흑야왕 사마공.

줄곧 미간을 좁힌 채 골똘히 생각에 잠겨 있던 그의 물음에, 갈수록 샛노래져 가던 마중걸과 그 수하들의 안색이 확 펴졌다.

“저, 저를 아십니까?”

“건너건너 들어 본 적은 있지. 십여 년 전 의문의 고수에 의해 녕하성의 마적단들이 평정되고, 그의 가르침으로 개심(改心)한 마적단의 두령 몇몇이 의기투합하여 마방을 세웠다고.”

“맞습니다! 그게 바로 저, 아니 저희입니다!”

이제야 말이 통하는 상대를 만났다는 듯, 혈색이 돌아온 마중걸이 문득 진중해진 얼굴로 모두를 향해 포권을 취했다.

“백마방주 마중걸. 그리고 백마칠종(白馬七宗)이 무림맹의 협객들을 뵙습니다.”

“……?”

“……?”

사방을 옥죄이는 숨 막히는 침묵.

흉악한 면상들과는 도무지 어울리지 않는 엘레강스한 별호에 나를 비롯한 수뇌부 전원은 말없이 시선을 교환했고, 마중걸의 뒤늦은 신호를 받은 여섯 사내는 어색하게 포권을 따라 하며 자기들끼리 속닥거렸다.

“그, 포권 이렇게 하는 거 맞습니까, 형님들?”

“이런 멍청한 놈. 오른 손바닥으로 왼손을 덮으라고 몇 번을 말했거늘.”

“뭔 소리요. 막내는 제대로 했구먼. 넷째 형님이 틀렸소.”

“어, 진짜네…….”

“갈. 모두 입 닥치지 못하겠느냐. 이게 어떤 자린 줄 알고.”

“에효. 조금 전까지는 아주 목이 터져라 갈갈 대다가 고수들 앞이라고 목소리 줄인 거 봐라. 내가 시부럴 늦게 태어난 게 죄지. 죄야.”

“…….”

이거 진짜 뭐 하는 새끼들이지?

한껏 목소리를 낮췄음에도 또렷하게 들려오는 대화 소리에 모두가 짜게 식은 눈빛이 된 그때, 유일하게 평정심을 잃지 않은 사마공이 입을 열었다.

“그래, 자네들 백마방에 관한 이야기는 몇 번 들어서 알고 있지. 북방의 대초원을 통해 침입한 유목민들과 맞서 싸우고, 새롭게 정착하기 시작한 양민들에게도 여러 도움을 준다 들었네. 한데…….”

말꼬리를 흐린 사마공의 눈빛이 불현듯 날카로워졌다.

“이렇게 갑작스럽게 찾아온 연유가 무엇인가?”

그리고 일순간 집중된 모두의 시선 속에서, 굽혔던 허리를 곧게 편 마중걸이 대답했다.

“도움을 드리고자 이리 찾아왔습니다.”

“도움이라면?”

“암천(暗天). 놈들에 관한 중요한 정보가 있습니다.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 1008

To cut to the chase, by the time the third volley of arrows had ended, the leaders of the Gansu Murim had decided to welcome the fifty-odd suspicious-looking men—including the giant—inside the gates.

Of course, saying the decision reflected the opinion of the entire leadership would be misleading.

Jeok Cheongang’s presence had played a very large part in it.

“I don’t know what hole these mangy mutts crawled out of, but let them in alive for now.”

Then he added, addressing the murmuring leaders:

“What are you sitting there agonizing over? If they seem suspicious, kill them and send them back out.”

“Oh.”

“Ah.”

It was such a clear-cut answer that even Judge Bao would’ve brought his dog-headed execution blade down with a smack. The meeting that hardly deserved to be called a meeting came to an end, and the Black Night King, Sima Gong, immediately ordered his subordinates to admit the hideous-looking unwelcome guests.

*Rumble, rumble.*

The massive iron gates began to open, little by little.

The giant was the first to step through the gap. He swept his bulging eyes around the area.

He’d damn near shit blood dodging three volleys of arrows, and now he looked like he’d been dragged through a shredder. His half-rolled eyes darted about, searching for someone.

Someone like the young bastard who’d suddenly ordered the archers to fire.

“Looking for someone? Keep that up and you’ll get a crick in your neck. Want me to find them for you?”

I’d come down first to greet our unexpected visitors. I tossed out the question as I stepped forward, and the giant’s eyes widened.

“You, you…!”

“I saw it all from up there. Nice job blocking them. Nice job dodging, too.”

“You pretty little gigolo-faced bastard, how dare you!”

“What did you just call me?”

Something in my expression hardened. At the strange pressure pouring off me, the giant flinched on instinct, then forced out another strained reply.

“I said you look like a pretty little gigolo…!”

“Hold on. Just hold on a second.”

“What?”

Leaving the giant’s angry, baffled question hanging, I closed my eyes.

*He said I look like a pretty little gigolo.*

What a wonderful thing to hear.

For a man of the same sex and the same chromosomes to say that to me was the highest praise imaginable.

I held on to the lingering swell of emotion washing over me, then opened my eyes.

“Thanks. Turns out you’re a good guy.”

“…?”

“So, where are you from, our Junggeol?”

“……!”

The giant—or rather, Ma Junggeol—nearly popped his eyes out of his head.

“How did you know?!”

“Hm? Know what?”

“My, my name.”

Seeing him stumble over his words now, I answered as casually as could be.

“Didn’t I tell you? We already introduced ourselves. You’ve forgotten that fast?”

“I…?”

“You must still be rattled. Fair enough. You had to dodge all those arrows.”

Ma Junggeol would probably never know.

At this very moment, a translucent holographic window was floating like a ghost above his head.

> **System**  
> **Level:** 80  
> **Name:** Ma Junggeol

Level 80.

A person’s level wasn’t an absolute measure of their strength, but even so, it was awfully low for someone I’d suspect of being a Dark Heaven lackey.

*Going by what I saw earlier, he’s maybe a fairly seasoned Peak master?*

Still, you couldn’t let your guard down so easily.

As I slowly looked over Ma Junggeol, who still seemed dazed, the leaders atop the wall finally appeared on the stairs, Jeok Cheongang among them.

At the same time, the fifty-odd mounted men came rushing toward us.

“Stop!”

“Let’s talk! Let’s talk!”

“We don’t want to fight!”

“Big Brother! Are you all right?”

“Enough!”

“I can’t believe this. I told you to stop doing that.”

Six men, riding side by side at the very front of the group, surrounded Ma Junggeol.

*What the hell are these guys?*

I was sure everyone there was thinking something much like I was.

The lanky one. The dwarf. The bulbous-nosed one. The tiny-eyed one…

Every one of them had striking features and facial parts that seemed to have gone their own way. It was a combination you didn’t see every day. And Ma Junggeol, standing in the middle of those six men, was the finishing touch.

*Was his father Picasso?*[^1]

They all had such strong impressionist faces that even the Black Dragon Demon Gate’s martial artists—who’d been through their share of life at the bottom—instinctively reached for their sword hilts.

*Shing.*

As the faint sounds of friction from here and there heightened the tension, a low voice reached everyone’s ears.

“I guarantee that any of you who try something stupid from this point on will be spending a very hot time with this old man.”

No one present needed to ask who’d spoken.

And, naturally, not even Tokyo Hot could hold a candle to the JCK-444 Fire Show Special. No one wanted to star in it.[^2]

*Clatter, clatter, clatter.*

The sea of people parted to either side, as though fleeing a raging inferno.

Jeok Cheongang emerged through the gap, leading the other leaders. He glanced at Ma Junggeol, then turned to me.

“So, who is he, and where did he come from?”

“His name is Ma Junggeol. I don’t know where he came from yet.”

“Could he be a Dark Heaven lackey?”

“We’d have to beat the truth out of him to be sure. But, as you already know, he doesn’t look or seem capable of pulling anything clever…”

“You can’t judge by appearances alone. What do you think about the possibility that they’re deliberately hiding their strength?”

Jeok Cheongang wasn’t asking because he didn’t know. He meant for everyone listening to our conversation to hear the question. Once I understood his intent, I answered without hesitation.

“None.”

“You must have a reason for thinking so.”

“Old man—no, Master, if they were strong enough to fool you and the others here, they’d have to have reached at least Returning to Simplicity or Bone Transformation.”

“And?”

“Look at those faces. Supreme Peak masters who’d reached that level couldn’t possibly look like that.”

“……!”

“……!”

The seven vicious-looking men, Ma Junggeol included, shuddered. What could I do? It was true.

I’d suddenly found myself playing lawyer, and I felt an inexplicable sense of duty as I continued.

“Therefore, I find no grounds to charge them with ‘vicious-looking men concealing their martial arts,’ and I rest my case.”

Jeok Cheongang nodded with an expression of admiration.

“Your words are so logical that even this old man hardly dares to argue.”

“Thank you.”

“But looking at those faces—whether they’re Yellow Turbans, Dark Heaven, or at the very least men who’ve taken up important posts in the Demonic Cult—I can’t help but find them suspicious.”

“So what are you going to do?”

“Either they confess everything right now, or I’ll beat it out of them with the Flame Divine Palm.”

His voice was directed at me, but his gaze wasn’t.

Under Jeok Cheongang’s stare, which seemed to pour streams of fire, Ma Junggeol went pale and stammered:

“A-are you really the Fire King, Jeok Cheongang, Great Hero…?”

Jeok Cheongang replied with a bored look.

“Of course I’m real. Did you think I was a fake?”

“If that’s true, then the pretty little gigolo—no, the young man—is the Blazing Flame Divine Dragon…”

It was my turn to speak.

With a broad smile at hearing that pleasant description again, I tried to comfort the terrified Ma Junggeol.

“Keep calling me pretty little gigolo. Make yourself comfortable. Come to think of it, I was rude, speaking casually to you all this time. I’m sorry. Okay?”

“N-no, that’s all right. But it seems there’s been a misunderstanding for a while now. May I say something to clear it up?”

“Now you’re talking. You should’ve said—spoken up sooner.”

“I was trying to explain, but you jumped straight to—”

“Go on, then. Get to the point.”

At my gentle but forceful urging, Ma Junggeol hesitated, then straightened his shoulders and cautiously addressed the leaders, Jeok Cheongang included.

“To cut to the chase, we came from Ningxia.”

“Hold on. Ningxia? Could you be…?”

As a thought suddenly crossed my mind and I frowned, Ma Junggeol hurriedly added:

“We’re not mounted bandits!”

Jeok Cheongang muttered:

“So that’s why their faces looked so suspicious. They’re those mounted bandits who’ve been spreading filth all over Ningxia Province.”

“I-it’s true that I briefly belonged to a band of mounted bandits, but that’s not who we are now…”

Just then, the Wind-and-Cloud Sword Lord cut in.

He eyed Ma Junggeol and his men with narrowed eyes.

“Infinite Life Buddha. I shouldn’t say this as a man who pursues the Way, but as Senior Jeok said, those faces are clearly from the profession.”

People nodded here and there in agreement.

Then, as if to prove why looks ruled modern society, the mood slowly turned hostile. One person’s lips parted.

“Ma Junggeol, Ma Junggeol… Could you be that very Ma Junggeol of Baekma Bang?”

It was the Black Night King, Sima Gong.

He’d been deep in thought with his brow furrowed. At his question, Ma Junggeol and his men—whose faces had been turning more and more yellow—visibly brightened.

“Y-you know me?”

“I’ve heard of you through the grapevine. More than ten years ago, an unknown master pacified the mounted-bandit gangs in Ningxia Province. A few of their leaders changed their ways under his guidance, joined forces, and founded a horse caravan.”

“That’s right! That’s me—or rather, that’s us!”

As though he’d finally found someone he could talk to, Ma Junggeol’s color returned. His expression grew serious as he saluted everyone with clasped hands.

“I am Ma Junggeol, Chief of Baekma Bang. The Seven Masters of Baekma Bang greet the heroes of the Murim Alliance.”

“……?”

“……?”

A suffocating silence pressed in from all sides.

Their elegant titles didn’t fit their vicious faces at all. The leaders and I silently exchanged glances, while the six men, prompted belatedly by Ma Junggeol, awkwardly copied his salute and whispered among themselves.

“Uh, is this how you do the salute, hyungs?”

“You idiot. How many times have I told you to cover your left hand with your right palm?”

“What are you talking about? The youngest did it right. Fourth Hyung’s the one doing it wrong.”

“Oh, you’re right…”

“Enough! Can’t you all shut up? Do you know what kind of place this is?”

“Sheesh. A minute ago you were shouting ‘Enough! Enough!’ at the top of your lungs. Now you lower your voice because there are masters around. Being born later is my fucking crime. My crime.”

“……”

What the hell was going on with these guys?

Their voices were low, but their conversation still came through clearly. Everyone’s eyes had gone flat and dead. Only Sima Gong managed to keep his composure as he spoke.

“Yes, I’ve heard about Baekma Bang a few times. I hear you’ve fought off the nomads who invaded through the northern Great Steppe and given plenty of help to the commoners who’ve only recently begun settling there. But…”

Sima Gong let his voice trail off. His gaze suddenly sharpened.

“What brings you here so abruptly?”

Under the concentrated gaze of everyone around him, Ma Junggeol straightened his bent back and answered.

“We came here to offer our help.”

“Help with what?”

“Dark Heaven. We have important information about them.”

“……!”

[^1]: Picasso was a modern Spanish painter whose work is associated with Cubism and other avant-garde styles. Taekyung jokes that the men’s faces look like impressionist paintings.

[^2]: Tokyo Hot is a Japanese adult-video studio. JCK-444 is presented here as a particularly fiery adult-video special.
```

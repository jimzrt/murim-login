<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0890.txt",
      "sha256": "85da9d96e942d4c359c8eacc1027c4b04fb32d10b7a59cb10eb4b6cda888da09",
      "bytes": 12975
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2d5dc0fc57820aad1c167823b60c2f3f8f1062ddff158b26864861c9acaa4225",
      "bytes": 1488
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "320ce751be3fb3e0a87bf53762efb7d7d993d82fdb6aaaeacad1a601ce4c4d7c",
      "bytes": 230284
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "b7f00685996eb3c9803d797e0fc5941961a9dfdf03bce7939e572650be3ebbfa",
      "bytes": 1511
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "143279a4252eeacbd21d3dc7a128951bc2d7bad1b7688b6a67277d08a5676c6e",
      "bytes": 628
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "c038ff6bf95fd55ab294f9e491d0f0d83f3ebfe2c4f93dfcf4ee30dd921023e2",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "406e8d498960f3dd49931dd1d5770361135be3518660d5213e41d0a8bd58ed91",
      "bytes": 796
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "0b1b31809302d07a38e524018733f8b57c0554a990b1dfd8c55235633c00d3f7",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "aa9980da7ee8781e8d076bbd29b16141f4eafa9cb2f50f22402aaf62ffda72eb",
      "bytes": 259889
    }
  ],
  "estimated_tokens": 10208
}
-->

# Durable State Update — Chapter 890

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
1 and safe_through 890. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 890. Profile updates may replace only one
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
  "chapter": 890,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 890,
    "continuity_sources": [890],
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
    "The imperial banquet is three days away; So Gyo says the coming battle may be fiercer than the one over a decade ago.",
    "So Gyo believes Jin Taekyung may be the person she seeks and the person foretold by “that person,” but has not confirmed it. She says only she and the Emperor know the secret she withheld from Baek Yeon.",
    "So Gyo recovered two matching, curved saber-like objects buried in the flower garden and wears one at each hip.",
    "Prince Shangshan remains in the enemy’s grasp; Taekyung believes the confrontation cannot be avoided and slips toward the Outer Palace to reach Jeok Cheongang.",
    "Taekyung encounters Jeong Hogun while attempting to pass the guards at the Outer Palace."
  ],
  "continuity_sources": [
    889
  ],
  "open_questions": [
    "Who is the person So Gyo seeks, and who foretold them?",
    "What secret do So Gyo and the Emperor share, and why would Jeok Cheongang joining Taekyung’s side be preferable to So Gyo?",
    "What will happen at the imperial banquet, and can Taekyung reach Jeok Cheongang?",
    "Who is So Gyo, and whom does she serve?",
    "What is the purpose of the two curved saber-like objects So Gyo recovered?"
  ],
  "safe_through": 889,
  "temporary_decisions": [
    "Render 곡도 descriptively as “curved saber”; do not treat it as a proper name.",
    "Retain “that person” for 그분; the foreteller is not identified in this chapter."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 문주     | **Sect Leader**                              |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 은형술 | **concealment technique** | Peak-level technique used by the Hidden Thread to erase his presence. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 정천호 | **Commander Jeong** | Commander of the Embroidered Uniform Guard procession. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 889
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 889
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 889
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 888
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language, using calm reassurances and strategic metaphors to maintain unity while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 884
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃890화



철컥. 철컥.

중갑 특유의 쇳소리와 함께 가까워지는 묵직한 발걸음.

불과 삼 장 거리의 어둠 속에 숨어 있던 나는, 갑작스러운 정호군의 등장에 심장이 쫄깃해지는 것을 느꼈다.

‘네가 거기서 왜 나와……?’

내궁을 담당하는 금의위, 그중에서도 천호씩이나 되는 놈이 왜 여기까지 싸돌아다니는지는 모르겠지만 한 가지는 확실하다.

지금처럼 가까운 거리에서, 어설프게 움직였다간 정천호에게 발각당할 수도 있다는 것.

‘젠장. 이럴 줄 알았으면 은형술(隱形術)부터 제대로 배워 두는 건데.’

후회가 밀려들었지만 이미 늦어도 한참 늦었다.

무림에서 살려고 아등바등 몸부림치다 보니 적천강을 만났고, 열화문의 명맥을 잇게 된 이후로는 화끈한 맞다이가 유일한 전공이자 교양 과목이 되어 버렸으니까.

열화문이 어떤 문파인가.

기록에 남아 있는 역대 문주들의 행적만 봐도 하나같이 빠꾸 없는 상남자들. 똥도 서서 쌀 것 같은 미친놈들이다.

장장 삼백 년에 걸쳐 정사마(正邪魔)를 가리지 않고 맞짱을 떠 온 근본 있는 힙스터 문파에서, 은형술이란 나약함의 상징이나 다름없었다.

심지어는 이백 년 전쯤 천하제일의 고수였다던 당대 열화문주는 이런 기록까지 남겼다.



은형술을 익히고 싶은가?

그렇다면 네놈은 남색가(男色家)다.



무림의 필수 생존 기술 중 하나인 은형술을 씹게이 무공 취급하는 저 패기를 보라.

21세기에서 저런 발언을 했다면 무지갯빛 몽둥이로 집단 린치를 당했겠지만, 다행인지 불행인지 이 세상은 야만으로 점철된 무림이었고 열화문의 명맥은 꾸준히 이어졌다.

문제는 바로 그 훌륭한 선조들의 방침에 따른 결과, 지금의 내가 엿 되게 생겼다는 거고,

‘아니, 시바. 그래도 삼백 년이나 됐으면 문주 한 명쯤은 은형술 익혔어야 하는 거 아니냐.’

입술이 바짝바짝 마른다. 긴장을 해서 그런지 오줌이 마려워지기 시작했다.

어느새 일장 앞까지 다가온 정호군은 딱딱한 얼굴로 경계를 소홀히 한 금위군들을 추궁하고 있었다.

“대답하라. 왜 지정된 근무 위치를 이탈했지?”

“죄, 죄송합니다. 빗줄기가 너무 거센 탓에 몸이 으슬으슬하여.”

“역심(逆心)을 품은 자들이 은밀히 황궁에 잠입했을 때도 그런 말을 할 텐가?”

“그럴 리 있겠습니까. 다만 진심으로 반성하고 있으니…….”

“변명은 집어치워라. 바로 위 상관이 누구인가?”

“그, 그것이.”

“말하기 싫은가 보군. 아니지, 근무를 소홀히 한 걸 보니 금위군으로 복무하는 것 자체가 싫었던 건가?”

“아, 아닙니다!”

“그럼 여기가 안이지 밖인가?”

“……?”

“……?”

뭐지. 헌터 훈련소가 생각나는데.

‘저 새끼 설마 시스템 사용자……?’

최대한 기척을 숨긴 채 상황을 지켜보던 내가 정호군에 대한 합리적 의심을 떠올리고 있던 그때, 귀를 의심케 만드는 한 마디가 귓가를 파고들었다.

“너희들은 오늘부로 금위군이 아니다. 지금 즉시 상관을 찾아가 지금 있었던 일을 알리고 관패(官牌)와 의복, 병장기 등을 반납하도록. 새로운 교대 인원이 파견되기 전까지 이곳은 본관이 직접 경계하겠다.”

“……!”

“……!”

그야말로 청천벽력 같은 소리였다.

잠시 비를 피해 처마 밑에 있던 금위군에게도, 그리고 정호군이 떠나기만을 오매불망 기다리고 있던 내게도.

“자, 장군!”

“군법(軍法)은 지엄한 법. 이건 금의위 천호로서 내리는 명령이다.”

안 돼. 그 자식 말 듣지 마.

어차피 이제 민간인이니까 그냥 한 대 쳐.

나는 간절한 마음으로 예비군. 아니 금위군 아저씨들을 응원했지만, 지금 막 전역 절차를 밟게 된 그들에게는 최소한의 이성이 남아 있었다.

까라면 까는 것이 군대요, 나는 새도 떨어트리는 고관대작들 모가지도 자르는 곳이 금의위 아닌가.

이런 상황에서 엿 드십쇼를 시전할 수 있는 부류는 딱 둘로 나뉜다.

미친놈이거나. 열화문 입문 희망자거나.

하지만 안타깝게도, 지금 정호군 앞에 선 두 사람은 그 어디에도 속하지 않은 정상인이었다.

“명을…… 따르겠습니다.”

힘없는 목소리로 대꾸한 그들은 죽립을 푹 눌러쓴 채 어딘가를 향해 터덜터덜 걸음을 옮겼다.

아니, 정확히는 옮기려 했다.

앞서 정호군이 그랬듯이, 전혀 예상치 못했던 누군가가 나타나기 전까지는.

“참으로 희한한 일이로군. 언제부터 금의위가 금위군의 해임을 그리 즉흥적으로 결정할 수 있었지?”

차륵.

긴 옷자락이 고여 있던 물웅덩이를 스친다. 끝없이 쏟아져 내리는 빗줄기 사이로 모습을 드러낸 한 사람의 모습에, 잠시 침묵하던 정호군이 입을 열었다.

“마 태감(太監)께서 이곳에는 무슨 일로 오셨습니까.”

“별일 아닐세. 잠시 외부의 일을 처리하고 돌아오는 길이었지. 한데…….”

동창의 이 인자이자 실질적인 수장인 그, 마삼보가 빙긋 웃으며 말을 이었다.

“앞서 했던 물음에 대한 답을 들을 수 있겠나. 정 천호.”

“……군법을 이행한 것뿐입니다.”

“물론 그렇겠지. 그대가 얼마나 훌륭하고 뛰어난 사람인지는 나도 알고 있으니. 하지만 말일세.”

그 순간. 여인과 사내 그 어딘가쯤에 머물러 있던 마삼보의 목소리가 깊게 내려앉았다.

“절차대로 하게. 절차대로.”

“그건…….”

“제아무리 금의위 아래에 금위군이 있다고는 하나, 정해진 수순이라는 게 있지 않겠나. 최종 처벌을 내릴 수 있는 권한은 명백히 저들의 상관에게 있지. 그것이 그대가 말하는 군법이고.”

“……!”

“내가 해 줄 말은 그것뿐일세. 혹시 할 말이 남았나?”

말없이 마삼보를 응시하던 정호군이 입을 열었다.

“아닙니다.”

“좋아. 그럼 기왕 이리 만난 김에 잠시 동행이나 할까?”

“동행, 말씀이십니까?”

“그래, 제법 오랜만에 보니 반갑기도 하고. 때마침 긴히 할 얘기도 있어서. 어차피 자네도 내궁으로 복귀하는 길 아니었나?”

아마도 정호군이 할 대답은 ‘아닙니다.’ 혹은 ‘지금은 곤란합니다.’였을 것이다.

표정 변화가 없는 얼굴임에도 불구하고, 찰나의 순간 그의 옆모습에서 마삼보를 향한 경계와 거부감이 드러났으니까.

그러나 결론만 말하자면, 마삼보가 반 박자 더 빨랐다.

“아, 괜찮다고? 좋아. 그대라면 그리 대답할 줄 알았지.”

제아무리 십여 년 전의 반란 직후 동창의 권한이 축소되고, 금의위가 득세하는 상황이라 해도 마삼보는 이미 오래전에 몸져누운 창공을 대신하여 동창을 이끄는 실질적인 수장.

뭐라 대꾸할 틈도 없이 자연스럽게 선수를 가져간 그는 능글맞게 웃으며 정호군의 어깨를 툭툭 두드렸다.

“자, 가세. 금의위에 전해 줄 것도, 들어야 할 것도 많아.”

초절정 고수인 동시에 능숙한 정치인인 마삼보는, 천상 무인(武人)이나 다름없는 정호군에게는 그야말로 최악의 상성.

단번에 흐름을 빼앗긴 그는 바위처럼 굳은 얼굴로 정호군을 따라 자리를 뜰 수밖에 없었다.

깜짝 해고 이벤트의 위기를 벗어난 두 금위군에게 엄중한 경고를 남기는 것을 잊지 않은 채.

“근무가 끝나는 즉시, 조금 전 있었던 일에 대해 상관에게 보고하라. 알겠는가?”

“아, 알겠습니다.”

“충!”

지금이야 무슨 말을 못 할까.

순식간에 군기가 바짝 들어간 금위군들의 힘찬 군례를 들으며 정호군은 돌아섰고, 마음속으로 안도의 한숨을 내쉬던 내 귓가에는 한 줄기 전음(傳音)이 날아들었다.

- 정확히 무슨 용무로 이곳까지 왔는지는 모르겠지만, 주위에 지켜보는 이목이 많으니 요령껏 잘 다녀오게. 나중에 내 따로 연통하지.

“……!”

황급히 고개를 돌리자 이쪽을 향해 눈을 찡긋하는 마삼보의 모습이 보인다.

‘눈치채고 있었어. 처음부터.’

살짝 놀라긴 했지만, 어찌 생각해 보면 당연한 일이었다.

마삼보는 초절정의 경지에 오른 은형술의 대가. 고금제일의 살수라 평가받는 살성만큼 뛰어나진 않더라도 내 어설픈 수법을 눈치채기에는 차고 넘치는 수준일 테니까.

‘처음부터 예상하고 찾아온 건가? 아니면 단지 우연히?’

글쎄, 잘 모르겠다.

그가 이곳에 나타난 이유도. 또 무림의 살수들을 끌어들이게 된 과정도.

다만 지금의 내게 중요한 사실은, 주위에 남아 있는 금위군 수준으로는 내 기척을 눈치챌 수 없다는 것이다.

쉬릭.

짙은 어둠 속에서, 나는 그림자처럼 나아갔다.

끝없이 쏟아지는 빗줄기와 요란한 뇌성벽력의 도움을 받으며.

그리고 몇 개의 전각과 담벼락을 뛰어넘었을 때쯤, 다른 금위군들의 대화 속에서 시기적절한 힌트를 얻을 수 있었다.

“자네, ‘그놈’ 봤나?”

“누구? 아, 알 것 같군. 괴물이 따로 없던데.”

“덩치만 큰 줄 알았더니 정말 오지게 처먹더군. 특히 오향장육을. 반 시진도 안 됐는데 벌써 스무 접시도 넘게 해치웠네. 숙수들은 벌써 난리야.”

“허어. 대강 들어서 알고 있긴 했는데, 그 정도란 말인가?”

“미친놈이 따로 없다니까. 이 속도로 한 달만 지나면 절강성 돼지는 그놈 주둥이로 다 들어가게 생겼다던데. 배 속에 축사라도 차릴 기세야.”

“대단하구먼. 한데 그 정도면 차라리 쫓아내는 게 낫지 않나?”

“황실 체면이 있지, 대연회를 위해 데려온 자들을 돼지고기 좀 먹는다고 박대할 수는 없지 않나. 이미 숙식 관련해서는 필요한 만큼 제공하라는 명령도 떨어진 마당에.”

“허어어어.”

이름을 부른 것도 아니고 ‘그놈’이라니.

괜히 나까지 부끄러워지는 것은 왜일까.

‘태산이 이 새끼…….’

하늘을 우러러 탄식하던 나는 문득 어딘가로 바쁘게 움직이는 일단의 무리를 발견했다.

숫자는 십여 명에, 각각의 손에 들린 커다란 접시들.

그리고 마지막으로, 축농증 환자도 코가 뻥 뚫릴 만큼 진한 오향장육의 냄새까지.

“……!”

일행들이 외궁 어딘가에 머무른다는 것만 알고 있었을 뿐. 배정받은 숙소 위치까지는 몰랐는데 이런 식으로 풀릴 줄이야.

‘이거 실화냐.’

나는 헨젤과 그레텔의 마음으로 그들의 뒤를 밟았다. 누구도 알아차릴 수 없을 만큼 조용히.

그리고 숙수로 보이는 중년인이 속사포처럼 내뱉는 쌍욕을 들으며.

“제발 좀 그만 처먹어라. 사람 새끼면 제발…….”

그 순간. 나는 똑똑히 봤다.

그의 다른 한 손에 쥐어진, 커다란 식도(食刀)가 파르르 떨리는 것을.



* * *



“음식 왔소.”

드르륵, 쾅!

깊게 가라앉은 목소리와 함께 전각의 문이 거칠게 열린 순간, 화왕 적천강은 두 번 놀랐다.

아무리 봐도 무공을 익히지 않은 것이 분명한 중년의 숙수가 제대로 된 살기(殺氣)를 내뿜고 있다는 것에 한 번.

그리고 피곤에 찌든 얼굴로 음식을 바리바리 싸 들고 온 그들의 뒤에, 익숙한 얼굴이 어둠 속으로 빼꼼 고개를 내밀고 있는 것에 다시 한번.

“저, 저……!”

“왜 그러시오?”

“아, 아무것도 아니오.”

“아무것도 아니면 음식이나 좀 받으시오. 팔 부러질 것 같으니까.”

날 선 목소리로 대꾸한 중년의 숙수는 함께 온 궁인들을 시켜 접시를 내려놓고는 사라졌다.

오늘 한 번만 더 오향장육을 주문한다면 독을 넣겠다는 경고와 함께.

그리고 그들이 사라지기 무섭게, 어디선가 불어온 바람이 금방 닫혔던 문을 열어젖혔다.

적어도 다른 누군가가 보기에는 그랬다.

“뭣 하느냐. 어서 안 들어오고.”

화왕 적천강이 불쑥 던진 한마디에, 어둠 속에서 불현듯 나타난 청년이 씩 웃었다.

“저 왔습니다.”
```

## Final English reading copy

```markdown
# Chapter 890

Clank. Clank.

Heavy footsteps drew closer, accompanied by the distinctive metallic clatter of heavy armor.

Hidden in the darkness just thirty feet away, I felt my heart seize up at Jeong Hogun’s sudden appearance.

*What the hell are you doing here…?*

I didn’t know why a Thousand Captain of the Embroidered Uniform Guard, responsible for the Inner Palace, was wandering around all the way out here. But one thing was certain:

At this distance, if I made even a clumsy move, Commander Jeong could spot me.

*Damn it. If I’d known this would happen, I should’ve learned the concealment technique properly first.*

Regret washed over me, but it was far, far too late for that.

I’d struggled tooth and nail to survive in Murim, and that was how I’d met Jeok Cheongang. Then, after inheriting the Fire Gate Clan’s legacy, a good old-fashioned brawl had become both my only major and my general-education requirement.

What kind of sect was the Fire Gate Clan?

Just look at the records of its past Sect Leaders. Every last one of them was a no-holds-barred tough guy. The kind of lunatic who looked like he’d take a shit standing up.

For three hundred years, this thoroughly established hipster sect had picked fights without distinguishing between the orthodox, unorthodox, or demonic paths. In a place like that, the concealment technique was practically a symbol of weakness.

One of the Fire Gate Clan’s Sect Leaders, said to have been the greatest master in the world some two hundred years ago, had even left behind this record:

> Want to learn the concealment technique?
>
> Then you’re a homosexual.

Behold the audacity of dismissing one of Murim’s essential survival skills as a martial art for fags.

If he’d said something like that in the twenty-first century, he’d have been beaten half to death with rainbow-colored clubs. But whether by good fortune or bad, this world was Murim, steeped in barbarism—and the Fire Gate Clan’s lineage had carried on uninterrupted.

The problem was that, thanks to the fine policies of those ancestors, I was the one about to get screwed now.

*Seriously, shit. In three hundred years, couldn’t one Sect Leader have learned the concealment technique?*

My lips were drying out. Maybe it was the nerves, but I was starting to need to piss.

Jeong Hogun had now come within ten feet. His expression hard, he was interrogating the Imperial Guard soldiers who’d neglected their duty.

“Answer me. Why did you leave your assigned post?”

“S-Sorry, sir. The rain was so heavy that we were shivering…”

“Would you say the same thing if someone harboring treasonous intentions slipped into the imperial palace undetected?”

“Of course not. We truly regret it, but…”

“Enough excuses. Who is your immediate superior?”

“W-Well, that is…”

“You don’t want to say? No, given how carelessly you’ve been doing your duty, perhaps you didn’t want to serve in the Imperial Guard at all?”

“N-No, sir!”

“Then is this the inside or the outside?”

“……?”

“……?”

What was this? It reminded me of Hunter boot camp.

*Is this bastard a System user…?*

As I watched the scene with my presence hidden as much as possible, entertaining a reasonable suspicion about Jeong Hogun, one remark made me doubt my ears.

“As of today, you are no longer members of the Imperial Guard. Go to your superiors immediately, report what happened here, and return your badges, uniforms, weapons, and the rest. I will guard this post myself until your replacements arrive.”

“……!”

“……!”

It was like a bolt from the blue.

For the soldiers who’d only taken shelter from the rain beneath the eaves—and for me, who’d been waiting with bated breath for Jeong Hogun to leave.

“G-General!”

“Military law is strict. This is an order from me as a Thousand Captain of the Embroidered Uniform Guard.”

No. Don’t listen to him.

You’re civilians now anyway. Just punch him once.

I fervently cheered on the middle-aged reservists—I mean, the Imperial Guard soldiers—but the two men who’d just been sent through the process of discharge still had a shred of reason left.

In the military, when they tell you to jump, you ask how high. And the Embroidered Uniform Guard was the place that could even cut off the heads of the highest officials—the sort who could make a flying bird drop from the sky.

Only two kinds of people could tell him to go to hell in a situation like this:

Lunatics. Or people hoping to join the Fire Gate Clan.

Unfortunately, the two men standing before Jeong Hogun were neither. They were perfectly normal.

“We’ll… obey your order.”

They answered in weak voices, pulled their rain hats low, and trudged off somewhere.

Or, to be precise, they tried to.

Just as with Jeong Hogun a moment ago, someone entirely unexpected appeared.

“How strange. Since when has the Embroidered Uniform Guard been able to dismiss Imperial Guard soldiers on a whim?”

Swish.

A long robe brushed across a puddle. Amid the endless sheets of rain, a figure emerged. Jeong Hogun was silent for a moment, then spoke.

“Eunuch Ma, what brings you here?”

“Nothing in particular. I was taking care of something outside and am on my way back. But…”

He, Ma Sanbao—the East Depot’s second-in-command and its de facto leader—smiled faintly before continuing.

“Could I have an answer to my earlier question, Commander Jeong?”

“……I was only enforcing military law.”

“Of course you were. I know what a fine and capable man you are. But…”

At that moment, Ma Sanbao’s voice, which had always seemed to hover somewhere between a man’s and a woman’s, dropped low.

“Follow procedure. Follow procedure.”

“That’s…”

“Even if the Embroidered Uniform Guard outranks the Imperial Guard, there’s still a proper process to follow, isn’t there? The authority to impose a final punishment clearly belongs to their superiors. That’s the military law you mentioned.”

“……!”

“That’s all I have to say. Is there anything else?”

Jeong Hogun gazed at Ma Sanbao in silence, then spoke.

“No.”

“Good. Since we’ve run into each other, why don’t we go together for a while?”

“Go together?”

“Yes. It’s been quite some time, and I’m glad to see you. I also have something important to discuss with you. You’re heading back to the Inner Palace anyway, aren’t you?”

Jeong Hogun had probably meant to answer, “No,” or “Now isn’t a good time.”

Despite his expressionless face, for just an instant his profile revealed his wariness and aversion toward Ma Sanbao.

But in the end, Ma Sanbao was half a beat faster.

“Oh, you don’t mind? Good. I knew you’d say that.”

Even though the East Depot’s authority had been curtailed after the rebellion more than a decade ago, and the Embroidered Uniform Guard had risen to prominence, Ma Sanbao was still the East Depot’s de facto leader, standing in for the seriously ill Cang Gong, who’d been confined to bed for a long time.

He smoothly seized the initiative before Jeong Hogun could get a word in, then smiled slyly and patted him on the shoulder.

“Come along. There’s plenty to tell the Embroidered Uniform Guard—and plenty to hear from them.”

Ma Sanbao was a Supreme Peak master and a skilled politician. For Jeong Hogun, who was all but a martial artist through and through, he was the worst possible opponent.

Having lost control of the conversation in an instant, he could only leave with his face rigid as a rock, following Jeong Hogun.

Not before leaving a stern warning for the two Imperial Guard soldiers who’d escaped the threat of a surprise firing, though.

“As soon as your shift ends, report what happened here to your superior. Understood?”

“Y-Yes, sir.”

“Understood!”

Of course they’d say yes now.

As I listened to the two soldiers, suddenly standing ramrod straight, give their hearty salute, Jeong Hogun turned away. I was breathing an inward sigh of relief when a strand of Sound Transmission reached my ear.

—I don’t know exactly why you’ve come all the way here, but there are many eyes watching. Be careful and use your wits. I’ll send word to you myself later.

“……!”

I whipped around. Ma Sanbao was looking this way and winking.

*He knew. From the beginning.*

It startled me a little, but when I thought about it, it made sense.

Ma Sanbao was a master of the concealment technique who’d reached the Supreme Peak realm. He might not be as skilled as the Slaughter Saint, hailed as the greatest assassin of all time, but he was more than good enough to notice my amateurish trick.

*Did he expect me and come looking? Or was it just a coincidence?*

Who knew?

I didn’t know why he’d appeared here. Or how he’d gotten the assassins of Murim involved.

But what mattered to me right now was that the remaining Imperial Guard soldiers weren’t skilled enough to detect my presence.

Whoosh.

I moved like a shadow through the thick darkness.

With the help of the relentless rain and the thunderous crashes of lightning.

After leaping over several pavilions and walls, I picked up a timely hint from a conversation between some other Imperial Guard soldiers.

“Did you see ‘that guy’?”

“Who? Oh, I think I know who you mean. He’s a monster, all right.”

“I thought he was just big, but he really does eat an insane amount. Especially five-spice pork. It hasn’t even been half a shichen, and he’s already eaten more than twenty plates. The cooks are making a fuss.”

“Good grief. I’d heard a little about it, but that much?”

“He’s a lunatic, I’m telling you. At this rate, they say he’ll eat every pig in Zhejiang Province with that mouth of his within a month. He looks like he’s got a pigsty in his stomach.”

“That’s impressive. But at that point, wouldn’t it be better to kick him out?”

“The imperial family has its reputation to consider. They can’t treat people brought here for the grand banquet poorly just because they eat a little pork. Orders have already been given to provide them with whatever they need for lodging and meals.”

“Good grief…”

They hadn’t even used his name. Just *that guy*.

Why was I embarrassed on his behalf?

*Taishan, you bastard…*

I sighed toward the heavens, then spotted a group of people hurrying somewhere.

There were more than ten of them, each carrying a large plate.

And, last of all, the rich smell of five-spice pork—strong enough to clear the nose of someone with sinusitis.

“……!”

I’d only known that the group was staying somewhere in the Outer Palace. I had no idea where they’d been assigned rooms. Who knew things would work out like this?

*Is this for real?*

I followed them like Hansel and Gretel, quietly enough that no one could notice.

And listened as a middle-aged man who looked like one of the cooks rattled off a string of curses.

“Please, just stop eating already. If you’re even human, for the love of—”

At that moment, I saw it clearly.

In his other hand, the large kitchen knife trembled.

* * *

“Food’s here.”

Creak—BANG!

The door to the pavilion flew open with a rough shove, and the Fire King, Jeok Cheongang, was surprised twice.

First, that a middle-aged cook who clearly hadn’t learned martial arts was giving off genuine killing intent.

Then, that behind the cook and his exhausted companions, who’d come carrying bundles of food, a familiar face was poking its head out from the darkness.

“Y-You…”

“What is it?”

“N-Nothing.”

“If it’s nothing, then take some of the food. My arms are about to break.”

The middle-aged cook answered sharply, then had the palace attendants who’d come with him set down the plates before leaving.

Not before warning them that if they ordered five-spice pork one more time today, he’d poison it.

And as soon as they were gone, a breeze from somewhere blew the door they’d just closed open again.

At least, that’s how it would have looked to anyone else.

“What are you waiting for? Get in here.”

At the Fire King Jeok Cheongang’s abrupt command, a young man suddenly appeared from the darkness and grinned.

“I’m here.”
```

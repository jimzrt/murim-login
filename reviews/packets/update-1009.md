<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1009.txt",
      "sha256": "b8689374b3e8f0d6cecfe110ae9f97a52291a7a018bfb13558acf68a823084c3",
      "bytes": 13210
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "261c7ef5ba62d8f9267168cdddf467104afa359d078b98c0f85fd2d57858e301",
      "bytes": 729
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b104545771a66a8fc3a9ca63e7f5e7da6a886d5b28c68d12d55267b0309741d3",
      "bytes": 237440
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "ecd7b844f1301a6e9984ebaff34ad29534efef701af9cd06d055cfa58be169c6",
      "bytes": 611
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "912732d4cfe4595f828879839c800845959dc4217c07168a7a6026bbc880a147",
      "bytes": 1408
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "14d12a6b38986fc8525ad0164eeca077c8d6ac9ad28c95486e3d96919648afb9",
      "bytes": 563
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "2817a92ff2a9a8b060bf59c117723f4a660cb33b48665df75c755beb9d88c54f",
      "bytes": 733
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "60df388ea1addfbf06f4f1e61d215dec707c276346f1f5038c80ce6896f8f7ca",
      "bytes": 276305
    }
  ],
  "estimated_tokens": 9551
}
-->

# Durable State Update — Chapter 1009

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
1 and safe_through 1009. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1009. Profile updates may replace only one
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
  "chapter": 1009,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1009,
    "continuity_sources": [1009],
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
    "Ma Junggeol leads Baekma Bang and arrived from Ningxia with six associates known as the Seven Masters of Baekma Bang.",
    "Baekma Bang was founded by former Ningxia mounted-bandit leaders reformed under an unknown master more than ten years ago; the group now fights steppe nomads and helps settlers.",
    "Ma Junggeol says Baekma Bang has important information about Dark Heaven and came to offer help."
  ],
  "continuity_sources": [
    1008
  ],
  "open_questions": [
    "Who was the unknown master who helped reform the Ningxia bandit leaders?",
    "What information about Dark Heaven does Baekma Bang possess?"
  ],
  "safe_through": 1008,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 암천     | **Dark Heaven**                  |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 마중걸 | **Ma Junggeol** |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 녕하성 | **Ningxia Province** | Region between Gansu and Shaanxi. |
| 멸지 | **Land of Ruin** | Name used for the desert region beyond which Dark Heaven’s forces are approaching. |
| 백마방 | **Baekma Bang** | Ma Junggeol’s horse-caravan group, founded by reformed mounted-bandit leaders. |
| 백마칠종 | **Seven Masters of Baekma Bang** | Collective title for Ma Junggeol and his six associates. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 마중걸 | 적천강 | visiting horse-caravan chief to legendary martial master | Great Hero Jeok Cheongang | polite and deferential | Recognizes Jeok as the Fire King. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |

## Listed compact profiles

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 982
- **Aliases:** None
- **Role:** Jamukha was the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek; Jin Taekyung killed him.
- **Personality:** Patient and ambitious, he was willing to feign loyalty to gain the power to rule the steppe and north.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared and recruited him, but Jamukha’s loyalty to him was feigned.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1008
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1008
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** He is initially confrontational under pressure but becomes formal and earnest when explaining his group’s purpose.
- **Voice:** Not established
- **Relationships:** He leads six associates who, with him, are known as the Seven Masters of Baekma Bang.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1008
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating, yet outwardly gentle; he uses persuasive sophistry and a calming manner to justify hard choices.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1009화



만약 마중걸이 조금이라도 수상쩍거나 시시껄렁한 이유를 댔다면, 즉각 성문 밖으로 쫓겨났거나 혹은 성안 어딘가에 있을 뇌옥에 처박혀 고문 기술자들과 많은 대화를 나누었을 것이다.

하지만 한껏 낮춰진 마중걸의 목소리에는 생각보다 중요한 이유가 담겨 있었다.

“암천(暗天). 놈들에 관한 중요한 정보가 있습니다.”

“……!”

그리고 그 한마디가 흘러나온 순간, 나를 포함한 모든 수뇌부는 눈앞의 불청객들이 생각보다 꽤 쓸모가 있을 거라는 사실을 깨달았다.

“이거, 귀한 손님들을 너무 오랫동안 밖에 세워 뒀군. 안에서 차라도 한잔 들지 않겠나?”

은근한 사마공의 물음에, 언제 그랬냐는 듯이 활짝 어깨를 편 마중걸이 고개를 끄덕였다.

“좋지요. 혹시나 하는 마음에 한 말씀 드리자면, 저와 제 아우들은 차 중에서도 곡차(穀茶)를 제일로 칩니다.”

“백마방의 일곱 의형제가 알아주는 주당들이라더니, 듣던 대로 아주 호쾌하군. 그럼 어서 안으로 들지.”

중요한 이야기는 지켜보는 이목이 적을수록 좋은 법.

그렇게 때아닌 불청객에서 귀빈으로 단숨에 위치가 격상된 마중걸과 여섯 사내. 아니 백마칠종(白馬七宗)이 대회의실에 한 자리씩 차지하게 된 것은 그로부터 촌각이 흐른 직후였다.

“크어어어. 좋다.”

마중걸을 시작으로 작은 술동이 하나를 단번에 비워 낸 그의 의형제들이 입맛을 쩍쩍 다셨다.

“어후, 진짜 끝내주네.”

“이거 무슨 술입니까? 혀끝에 닿자마자 아주 사르르 녹는데요.”

“그러게. 미쳤다.”

“……아니, 술이니까 당연한 거 아니오? 사르르 녹기는 개뿔이. 이러니까 멍청하다는 소리를 듣지.”

“갈. 넷째 네 이놈. 형제들에게 그 무슨 말버릇이냐.”

“어후, 숨통 좀 트였다고 다시 목소리 커진 거 봐. 내 진짜 맘 같아서는 지금 당장이라도 이 술동이로 뒤통수를 그냥.”

물론 당연하게도, 누군가의 머리통과 술동이가 부딪치는 불상사는 일어나지 않았다.

일곱 빛깔 마적 레인저, 아니 백마칠종을 말없이 바라보던 적천강의 한마디 때문이었다.

“술 처먹으러 왔느냐?”

“……!”

“……!”

“이제 목도 축였으니 어디 한번 씨부려 보거라.”

적천강에게서 흘러나오는 험악한 기세에 순간 움찔한 마중걸이, 더듬더듬 입을 열었다.

“우, 우선은 녕하 일대의 사정에 대해서는 이미 어느 정도 알고 계시리라 생각합니다.”

“대충은 들었지. 너희 같은 마적 놈들 때문에 말판 촌각 전까지 갔다가 근 몇 년 동안은 잠잠해졌다고. 맞느냐?”

“저희는 더 이상 마적이 아니지만, 예. 적 대협의 말씀이 맞습니다.”

“그래 봤자 노부가 보기에는 아직도 마적 나부랭이지만, 일단은 계속해라.”

“그간 사소한 분란이 몇 번 일어나긴 했지만, 이제는 제법 살기 좋은 땅이 됐습니다. 뭔가 켕길 만한 짓거리를 한 번이라도 했던 놈들은 진즉 떠났고, 남은 놈들은 저나 제 아우들처럼 완전히 개심하여 평범하게 살아가고 있습니다. 이 부분은 여기 계신 사마 문주께서도 잘 아실 것입니다.”

자연스럽게 모여드는 사람들의 시선에, 사마공이 담담한 얼굴로 고개를 끄덕였다.

“사실이오. 녕하성이 안정되면서 여러 상단이 드나들기 시작했고, 그들을 통해 여러 정보를 들었지. 백마방에 관한 이야기도 그때 처음으로 알게 되었소.”

사마공의 지원사격을 받은 마중걸이 잽싸게 말을 받았다.

“사마 문주께서 정확히 어떤 이야기를 들으셨는지는 모르겠지만, 현재 저희 백마방의 규모는 녕하성에서도 단연코 으뜸입니다. 특히 최근에는 녕하성의 부흥을 도모하기 위해 새로운 상로(商路)까지 개척하고 있지요.”

“잠깐. 자네가 말한 새로운 상로라는 것이 혹시……?”

“아마 짐작하시는 그곳이 맞을 겁니다.”

마중걸의 대답을 들은 사마공의 얼굴 위로 놀라움이 번졌다.

그리고 그런 그의 모습을 보고 있자니, 문득 뇌리를 스치는 어떤 생각이 있었다.

“서쪽. 서쪽이군요.”

“……!”

내가 불쑥 내뱉은 한마디에, 보이지 않는 파장이 주위를 휩쓸었다.

당연한 일이었다.

내가 말한 서쪽은, 감숙도 청해도 아니었으니까.

“신강(新疆)…….”

신음과도 같은 음성이 풍운검군의 입술 사이를 비집고 흘러나왔다.

아까부터 뭐가 그리 마음에 안 드는 것인지, 탐탁지 않은 시선으로 마중걸을 지켜보고 있던 태을무정검과 노호검객 역시 눈살을 찌푸리며 입을 열었다.

“무슨 소리를 하나 했더니, 신강이라. 허.”

“나 참. 더는 못 들어 주겠군. 언제까지 이런 허무맹랑한 소리를 듣고 있을 거요?”

굳이 인정해 주긴 싫지만, 저 두 사람의 반응이야말로 지극히 상식적이었다.

신강이 어떤 곳인가.

멸지(滅智)로까지 불리는 땅이다.

끝없이 펼쳐진 사막과 마도천하(魔道天下)를 부르짖는 악귀들이 득실거리는 저주받은 땅.

그런데 구파일방이나 오대세가도 아닌, 일개 마방 따위가 신강으로 상로를 개척한다?

‘웃기지도 않은 소리지.’

하지만 그와는 반대로, 나는 조금씩 빠르게 뛰기 시작하는 심장 박동을 느끼고 있었다.

태을무정검과 노호검객은 가장 중요한 사실을 잊었다.

이 자리는 투자를 권유하는 자리도, 사업설명회도 아니라는 것을.

마중걸의 이야기는 아직 끝나지 않았으며, 오히려 지금부터가 진짜 시작이라는 것을.

“서두가 길었군. 그렇지 않으냐?”

착 가라앉은 적천강의 물음에 담긴 의미는 명백했고, 크게 심호흡한 마중걸이 재차 입을 열었다.

“비록 안정을 되찾았다 한들, 녕하성의 사정은 여전히 좋지 않았습니다. 땅은 척박하고 경계가 맞닿아 있는 대초원의 유목민들은 추수철만 되면 약탈을 자행했지요. 이런 상황을 타개하기 위해서는 새로운 탈출구가 필요했습니다.”

“해서, 사막을 넘어 상로를 뚫고자 했다?”

“그랬습니다만, 어디까지나 단순한 희망에 불과했습니다. 아무리 못 배운 놈이어도 그렇지 어디 저희 같은 놈들이 언감생심 꿈이나 꿀 수 있었겠습니까. 한데…….”

마중걸의 시선이, 문득 나를 향해 움직였다.

“얼마 전, 생각지도 못한 기회가 찾아왔지요. 대초원 서쪽을 차지하고 있던 수많은 유목민이 갑작스럽게 대이동을 시작한 겁니다.”

“……자무카.”

반사적으로 입술 사이를 비집고 튀어나온 한 사람의 이름.

나는 그제야 마중걸의 시선에 담긴 의미를 깨달았다.

그가 앞서 언급했던, 생각지도 못한 기회가 어떤 것이었는지도.

서부 초원을 장악하고 있던 자무카의 대군세.

놈들은 거의 모든 전력을 이끌고 산서성으로 진군했고, 그로 인해 생겨난 공백이 곧 백마방에게 있어 절호의 기회가 된 것이다.

“그렇다면 혹시, 초원을 통해 신강을 넘으려고 한 겁니까?”

내 물음과 함께 곳곳에서 헛숨을 삼키는 소리가 흘러나왔다.

맞다.

어느 순간 당연해졌고, 그렇기에 모두가 잊고 있던 또 하나의 선택지.

중원인들의 시선으로는 지금껏 신강과 더불어 또 하나의 금지(禁地)로 여겨졌던 대초원이야말로, 사막을 넘어설 수 있는 가장 빠른 지름길이었다.

그리고 모두의 집중된 시선 속에서, 마중걸은 긴장된 얼굴로 고개를 끄덕였다.

“그렇습니다.”

“……!”

“기마술에 능한 수하들을 선별해서 쉬지 않고 말을 몰았습니다. 그렇게 꼬박 열흘을 미친 듯이 내달리고 나니, 어느 순간 저 멀리에서 싯누런 땅이 보이더군요. 마침내 사막에 도착한 겁니다.”

그때, 마중걸의 뒤에서 눈치를 살피고 있던 여섯 의형제가 고개를 주억거리며 입을 열었다.

“어이고, 진짜 난리도 아니었지. 솔직히 그때는 대형이고 나발이고 죄다 엎어 버리고 돌아가고 싶었소.”

“한데 뭘 어쩌겠수. 거기까지 간 마당에. 기왕 온 거, 모래라도 좀 밟고 돌아가자 했던 거지.”

“그렇게 또 한 열흘쯤 갔었죠, 아마?”

“말도 마라. 지금도 그 염병할 사막만 떠올리면 오금이 저린다.”

“갈. 이런 나약한 놈들을 보았나. 나는 그 힘든 상황 속에서도 대형을 믿고 따랐다.”

제법 나이가 있어 보이는 난쟁이 중년인의 준엄한 일갈에, 주먹코 사내가 코웃음을 쳤다.

“말발굽이 삐뚤어져도 고삐는 바로 잡으랬다고, 제발 말은 똑바로 합시다. 열흘째 되던 날 그 시커먼 놈들이 나타나자마자 둘째 형님은 어찌했소? 뒤도 안 돌아보고 바로 도망칠 준비부터 했잖아.”

“갈……!”

얼굴이 홍시처럼 달아오른 난쟁이가 주먹코에게 달려들었지만, 그보다 내가 훨씬 빨랐다.

덥석.

손아귀 안에 정확히 안착하는 아담한 크기의 주먹.

허무하리만치 쉽게 난쟁이의 일권을 잡아챈 나는, 착 가라앉은 눈빛으로 주먹코를 응시했다.

“다시.”

“뭐, 뭐요?”

“방금 말했잖습니까. 사막에 들어선 지 열흘째 되던 날, 시커먼 놈들이 나타났다고.”

빠르게 지나가는 말이었지만, 나를 포함한 이 자리의 모두가 똑똑히 들었다.

그리고 들음과 동시에 머릿속에 떠오른 짐작은, 이내 확신으로 변했다.

“암천(暗天)이었습니다.”

주먹코 대신 입을 연 마중걸이 말을 이었다.

“머릿수는 수십여 명에 불과했지만 틀림없습니다. 제 목을 걸지요.”

사마공이 무거운 목소리로 입술을 뗐다.

“그렇게까지 확신할 수 있는 근거는?”

“놈들의 뒤를 밟았습니다.”

“뭣이?”

“딱 하루하고도 반나절. 그게 최선이었습니다. 하지만 이 두 눈으로 똑똑히 보았지요. 달이 유난히도 밝았던 그 날, 족히 일천에 달하는 천막이 사구(砂丘)를 뒤덮고 있었습니다.”

“……!”

“서쪽 사막에서 그 정도의 대병력을 동원할 수 있는 세력은 한 곳밖에 없지요. 암천. 그렇지 않습니까?”

대답 대신 싸늘한 침묵만이 회의실 안을 감돌았다.

일천. 사람도 아니고 천막의 개수가 무려 일천이라고 했다.

게다가 마중걸이 사막을 횡단한 경로는 명백하게 청해보다 감숙에 가깝다.

이는 아무리 낮게 잡아도 최소 수천, 혹은 수만에 달하는 적들이 감숙성을 노리고 있다는 뜻.

‘심지어 그마저도 전부가 아닐 수 있다.’

머릿속이 차갑게 식었다. 그와는 반대로 속도를 더해 가던 심장 박동은 어느덧 천둥처럼 귓가에 울려 퍼지는 중이었다.

물론 확신하기에는 아직 이르다.

결정을 내리기에 앞서, 해소해야 할 의문이 있었으니까.

“용케도 살아 돌아왔군.”

사마공의 나직한 음성이 찰나의 침묵을 깨트린다.

심유하기 그지없는 그의 눈빛에, 마중걸이 바짝 마른 입술을 핥았다.

“아슬아슬했습니다. 심장이 터져 죽는 줄 알았지요.”

“어떤 의미인지 알 텐데. 애써 모르는 척하는 것인가?”

“백 리. 딱 백 리의 간격을 두고 뒤쫓았습니다. 처음에만 고생했지, 그 후로는 시시각각 머릿수가 불어난 덕분에 훨씬 수월하더군요.”

“일개 마방들이 암천의 눈을 피해 추격한다라, 그게 가능한가?”

“부끄럽지만, 저희가 평범한 마방은 아니지 않습니까. 변발만 안 했지, 기마술이나 눈 밝은 것으로는 유목민들과 다를 것도 없습니다.”

“놈들을 발견하자마자 바로 돌아올 수도 있었을 터, 왜 하루하고도 반나절을 더 쫓았지?”

“그, 그것은…….”

잠시 머뭇거리던 마중걸이, 사마공을 힐끔거리며 조심스럽게 입을 열었다.

“천하를 위해 공을 세운다면, 출신 성분을 따지지 않는다 들었습니다.”

“보상을 생각했다?”

“예.”

쉽게 눈에 띄지 않을 만큼 소수의 인원이었던 데다, 잔뼈 굵은 마적 출신이라 가능했던 일.

게다가 그 이유 역시 명백하다.

잠깐의 고민을 끝마친 나는, 적천강을 향해 입을 열었다.

“이제 확실해졌네요. 저희가 머물러야 할 전장이 어디인지.”
```

## Final English reading copy

```markdown
# Chapter 1009

If Ma Junggeol had given even the slightest suspicious or flimsy reason, he would’ve been thrown straight back out the gate—or stuffed into the underground prison somewhere inside the city to have a long chat with the torture specialists.

But the reason Ma Junggeol gave in his lowered voice was more important than I’d expected.

“Dark Heaven. I have important information about them.”

“……!”

The moment those words left his mouth, all of us in the leadership—including me—realized that our unwelcome visitors might be a lot more useful than we’d thought.

“Well, we’ve kept our distinguished guests standing outside for far too long. Why don’t you come in and have a cup of tea?”

At Sima Gong’s subtle invitation, Ma Junggeol, who’d straightened his shoulders as though nothing had happened, nodded.

“Sounds good. Just so you know, of all the teas, my brothers and I favor grain tea most.”

“I heard the Seven Masters of Baekma Bang were renowned drinkers. You’re every bit as forthright as they say. Come on in, then.”

Important conversations were best held where fewer people could listen in.

And so, in the space of a few moments, Ma Junggeol and his six men went from unwelcome guests to honored visitors. Or, more accurately, the Seven Masters of Baekma Bang took their places in the grand meeting hall.

“Ahhh. That’s good.”

Starting with Ma Junggeol, his six sworn brothers drained a small wine jar in one go, then smacked their lips.

“Whew, that’s really something.”

“What kind of liquor is this? It just melts on your tongue.”

“Right? It’s insane.”

“……Isn’t that what liquor does? It’s liquor, so of course it melts. What do you mean, it melts? This is why people call you idiots.”

“Enough! Fourth, is that any way to speak to your brothers?”

“Whew, look at you raising your voice again the second you’re out of trouble. Honestly, if I had my way, I’d crack this wine jar over your head right now.”

Naturally, no one’s head and a wine jar met in a tragic collision.

That was thanks to Jeok Cheongang, who’d been silently watching the seven-colored mounted-bandit rangers—or rather, the Seven Masters of Baekma Bang.

“Did you come here to drink?”

“……!”

“……!”

“You’ve wet your throats. Now, go on and spit it out.”

Ma Junggeol flinched at the menacing aura rolling off Jeok Cheongang. Then he stammered out a reply.

“F-first, I assume you already know something about the situation in Ningxia.”

“I’ve heard the basics. Because of mounted bandits like you, the place nearly became a battlefield, but it’s been quiet for the past few years. Is that right?”

“We’re no longer mounted bandits, but yes. Great Hero Jeok is right.”

“Still look like a bunch of mounted bandits to this old man, but go on.”

“There’ve been a few minor disputes over the years, but it’s become a fairly livable place. Anyone who’d done something they might feel guilty about left long ago. The ones who remain have completely turned over a new leaf and live ordinary lives, like me and my brothers. Sect Leader Sima here knows this well, too.”

Everyone’s eyes naturally turned to him. Sima Gong nodded calmly.

“It’s true. As Ningxia Province settled down, various merchant caravans began passing through, and we heard all sorts of things from them. That was when I first heard about Baekma Bang.”

Bolstered by Sima Gong’s support, Ma Junggeol quickly picked up the thread.

“I don’t know exactly what you heard, Sect Leader Sima, but Baekma Bang is by far the largest group in Ningxia Province. Recently, we’ve even been opening a new trade route to help Ningxia Province prosper.”

“Wait. This new trade route you mentioned—is it perhaps…?”

“It’s probably where you’re thinking.”

Surprise spread across Sima Gong’s face at Ma Junggeol’s answer.

Watching him, a thought suddenly crossed my mind.

“To the west. It’s west.”

“……!”

My sudden words sent an invisible ripple through the room.

Naturally.

The west I meant wasn’t Gansu or Qinghai.

“Xinjiang…”

The word slipped through the Wind-and-Cloud Sword Lord’s lips like a groan.

The Taeeul Merciless Sword and the Roaring Fury Swordsman had been watching Ma Junggeol with obvious disapproval for a while now, as though something about him rubbed them the wrong way. They frowned and spoke up, too.

“So that’s what this is about. Xinjiang, huh. Hah.”

“I can’t listen to this anymore. How long are we supposed to sit here listening to such ridiculous nonsense?”

Much as I hated to admit it, those two were the ones reacting in the most reasonable way.

What kind of place was Xinjiang?

It was even called the Land of Ruin.

A cursed land of endless deserts and Fiends who proclaimed the world belonged to the Demonic Path.

And a mere horse-caravan group—not one of the Nine Sects and One Gang or the Five Great Families—was supposed to open a trade route to Xinjiang?

*What a joke.*

But at the same time, I could feel my heart starting to beat faster and faster.

The Taeeul Merciless Sword and the Roaring Fury Swordsman had forgotten the most important thing.

This wasn’t a pitch for investment or a business presentation.

Ma Junggeol’s story wasn’t over yet. In fact, the real story was just beginning.

“That’s enough preamble, isn’t it?”

Jeok Cheongang’s low question left no doubt what he meant. Ma Junggeol took a deep breath and spoke again.

“Even after things settled down, Ningxia Province was still in bad shape. The land was barren, and the nomads from the Great Steppe along our border raided us every harvest season. We needed a new way out to change things.”

“So you wanted to cross the desert and open a trade route?”

“That was the idea, but it was nothing more than a pipe dream. Even an uneducated fool like me knew people like us couldn’t seriously dream of something so far beyond our reach. But…”

Ma Junggeol’s gaze suddenly shifted toward me.

“Not long ago, an opportunity came out of nowhere. The many nomads occupying the western Great Steppe suddenly began a mass migration.”

“Jamukha.”

A name slipped from my lips before I could stop it.

Only then did I understand what Ma Junggeol meant when he’d talked about an unexpected opportunity.

Jamukha’s massive army had controlled the western steppe.

They’d taken almost all their forces and marched into Shanxi Province. The void they left behind had become a golden opportunity for Baekma Bang.

“Then were you trying to reach Xinjiang through the steppe?”

At my question, gasps came from around the room.

That was right.

The other option—the one that had become so obvious that everyone had forgotten it—was the Great Steppe, which the people of the Central Plains had long considered another forbidden land alongside Xinjiang.

It was the fastest route across the desert.

Under everyone’s focused gaze, Ma Junggeol nodded, his face tense.

“That’s right.”

“……!”

“I picked out the men under me who were good riders, and we kept driving our horses without stopping. After riding like mad for ten whole days, we finally saw a vast yellow stretch of land in the distance. We’d reached the desert.”

Just then, his six sworn brothers, who’d been keeping an eye on everyone’s reaction behind him, nodded and chimed in.

“Man, it was a real shitshow. Honestly, I wanted to say to hell with the Chief and the whole damn venture and turn back.”

“But what could we do? We’d already come that far. We figured, since we were there, we might as well step on the sand before we went home.”

“Then we traveled for another ten days or so, right?”

“Don’t remind me. Even now, just thinking about that goddamn desert makes my knees buckle.”

“Enough! You bunch of weaklings. Even in those hard times, I trusted the Chief and followed him.”

The diminutive middle-aged man, who looked rather old, delivered a stern rebuke. The man with the bulbous nose snorted.

“They say even if a horse’s hooves go crooked, you should keep a firm grip on the reins. So at least get your story straight. When those black bastards showed up on the tenth day, what did you do, Second Hyung? You didn’t even look back—you went straight to getting ready to run.”

“Enough…!”

The dwarf’s face turned as red as a ripe persimmon. He lunged at the bulbous-nosed man, but I was much faster.

*Snatch.*

A small fist landed perfectly in my grasp.

I’d caught the dwarf’s punch with ridiculous ease. I fixed the bulbous-nosed man with a cold stare.

“Say that again.”

“W-what?”

“You just said those black bastards appeared on the tenth day after you entered the desert.”

He’d said it in passing, but every one of us in the room had heard him clearly.

And the moment we heard it, the suspicion that arose in our minds turned to certainty.

“It was Dark Heaven.”

Ma Junggeol spoke up in place of the bulbous-nosed man and continued.

“They numbered only a few dozen, but I’m certain. I’ll stake my life on it.”

Sima Gong spoke in a grave voice.

“What makes you so certain?”

“We followed them.”

“What?”

“We managed a day and a half. That was the best we could do. But I saw it with my own eyes. That night, when the moon was unusually bright, at least a thousand tents covered the sand dunes.”

“……!”

“There’s only one force in the western desert that could mobilize an army that large. Dark Heaven. Isn’t that right?”

A cold silence filled the meeting hall instead of an answer.

A thousand. Not a thousand people—he said there were a thousand tents.

What’s more, Ma Junggeol’s route across the desert was clearly closer to Gansu than Qinghai.

That meant at least several thousand, perhaps tens of thousands, of enemies were targeting Gansu Province.

*And even that might not be all of them.*

My mind went cold. Meanwhile, my heartbeat had grown so fast it was thundering in my ears.

Of course, it was too soon to be certain.

There was still a question I needed answered before I could decide anything.

“You’re lucky you made it back alive.”

Sima Gong’s low voice broke the momentary silence.

Under his deep, penetrating gaze, Ma Junggeol licked his parched lips.

“It was close. I thought my heart was going to burst.”

“You know what I’m asking. Are you pretending not to?”

“We kept a distance of exactly a hundred li. It was hard at first, but after that it got much easier as their numbers kept growing by the hour.”

“An ordinary horse-caravan group following Dark Heaven without being spotted. Is that possible?”

“I’m ashamed to say it, but we’re not an ordinary horse-caravan group, are we? We may not wear our hair in queues, but when it comes to riding or having a sharp eye, we’re no different from the nomads.”

“You could have turned back as soon as you spotted them. Why follow them for another day and a half?”

“That… that’s…”

Ma Junggeol hesitated for a moment, glanced at Sima Gong, then cautiously spoke up.

“I’d heard that if you render a service for the good of the realm, no one cares where you came from.”

“You were thinking about a reward?”

“Yes.”

It had been possible because they were a small group that was hard to spot, and because they were former mounted bandits who’d learned how to survive.

And their reason was clear, too.

After a moment’s thought, I turned to Jeok Cheongang and spoke.

“Now I know for sure where we need to fight.”
```

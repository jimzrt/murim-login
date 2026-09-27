<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1085.txt",
      "sha256": "e75c0d3f352ef2536f08c71968b5ab7c9c0339c863b4b489c14506e1d49e4657",
      "bytes": 12484
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "55eeb1cbe680fda265873553974b90edfaf75819fd4c91ef73663dc73a800772",
      "bytes": 1018
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "598e1d5c5b60bfe97c315f4cdc530e9872755c5be7fc01ada06b463a73fa6a67",
      "bytes": 243586
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "95a41ccd1e733aa82fb4f5fec38e73729b6252b1e19cc79c437ea4c9473a7661",
      "bytes": 767
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "2280e14a9a4922f580e2c5809883ad5db2c8952a0443d911b0046bc0d003331f",
      "bytes": 686
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "011c64b15f964733a887933d3e6fddc2ffb3214cf706ca00e356d2e4ee5c3605",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "58a26ebc062bb2491d81493f3106d1710fa81b7f7ba862172b209911bfd6e6ec",
      "bytes": 286576
    }
  ],
  "estimated_tokens": 9649
}
-->

# Durable State Update — Chapter 1085

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
1 and safe_through 1085. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1085. Profile updates may replace only one
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
  "chapter": 1085,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1085,
    "continuity_sources": [1085],
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
    "The Yangtze River Channel League attacks the Great Nation’s military fleet under Pa Ryun’s command.",
    "Mu Song and the Iron-Water Divine Dragon opposed the League’s decision to join Dark Heaven and betray the Murim Alliance, but Pa Ryun’s decision stood.",
    "Mu Song ordered his men to spare the government soldiers aboard the ships they boarded.",
    "The League sank more than a hundred military vessels carrying thousands of troops in two shichen, then turned west."
  ],
  "continuity_sources": [
    1084
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who is the black-robed man beside Pa Ryun?"
  ],
  "safe_through": 1084,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 제갈세가   | **Zhuge Clan**                   |
| 남만야수궁  | **Nanman Beast Palace**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 삼고초려 | **Three Visits to the Thatched Cottage** | Allusion Zhuge Gyun uses to justify choosing the third option. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 녹림도 | **Green Forest bandit** | Bandit belonging to the Green Forest Alliance. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 제갈공명 | **Zhuge Kongming** | The Zhuge Clan's famous ancestor. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 북해빙궁 | **North Sea Ice Palace** | Isolationist Outer Murim faction. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 화원 | **Fire Courtyard** | Courtyard associated with Jin Taekyung and Ju Hwaran's final walk before leaving Sichuan. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 역천 | **defying heaven** | Supernatural power that regenerates the masked man's body. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 제갈풍 | 송호 | Zhuge Clan Family Head to Hidden Shadow Pavilion Chief | Chief of the Hidden Shadow Pavilion | formal and playfully accommodating | Zhuge Feng jokes that he would overlook Song Ho’s conduct if the amount were reasonable. |

## Listed compact profiles

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 997
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1082
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 998
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
1085화




소문은 순식간에 퍼졌다.

입에서 입으로.

전서구의 날갯짓으로.

채찍질에 따라 산과 들을 질주하는 말발굽과 하늘을 뿌옇게 물들이는 봉화(烽火)의 연기로.

그리고 이 엄청난 소문을 듣고 동요한 사람들이 진위 여부를 가리기도 전에, 그들은 두 눈으로 똑똑히 볼 수 있었다.

쾌속하게 강물을 가르며 나아가는 수많은 선박과 순풍을 받아 위풍당당하게 흩날리는 깃발들을.

장강수로맹(長江水澇盟).

순풍을 받아 한껏 부풀어 오른 깃발에 적혀 있던 다섯 글자를 확인한 순간, 사람들은 더 이상의 부정은 현실 도피나 다름없다는 사실을 깨달았다.

이제 그들이 보고 들은 모든 것은 헛소문 따위가 아니었다.

진실이었다.

천하의 묵인하에 장강에 기생하여 살아가던 한낱 수적들이, 마침내 장강의 진정한 지배자로 거듭난 것이다.

그것도 무려 천하의 주인인 대국을 상대로.

“……천지신명(天地神明)이시여.”

누군가의 입술 사이로 흘러나온 침음은 공허했다.

바로 그 천명(天命)을 받아 세워진 이 거대한 제국이 몰락하고 있었으니까.

아니, 그들의 하늘이.

“이것이 역천(逆天)이 아니라면, 도대체 무엇이 역천이란 말인가!”

군웅할거의 시대가 종막을 고하고 통일 왕조가 탄생한 지 어언 일백여 년.

천자가 다스리는 대국을 하늘로 떠받들던 촌부들은 불안에 떨었고, 당연했던 이치가 무너졌음을 깨달은 유생들은 신음했으며, 배신당한 무림인들은 분노와 경악에 휩싸였다.

“저 도적놈들이 기어코……!”

“처음부터 석연치 않았소. 애당초 흑도(黑徒) 따위를 믿어선 안 되었단 말이오!”

하지만 모두를 충격에 빠트린 소식은 장강수로맹의 배신만이 아니었다.

“이틀 전, 호북과 섬서 일대에서 녹림도들이 반기를 일으켰다고 합니다!”

장강수로맹과 함께 천하의 흑도를 양분하는 녹림맹의 준동.

그리고 거기에 더하여, 저 머나먼 장성(長城) 밖에서도 먹구름이 몰려들고 있음을 사람들은 뒤늦게 알아차렸다.

“사천에서 전해온 급보요! 서장(西藏)의 포달랍궁(布達拉宮)이 움직이고 있소!”

포달랍궁.

북해의 빙궁, 남만의 야수궁과 함께 새외삼세(塞外三勢)라 일컬어지는 밀승(密僧)들이 마침내 오랜 침묵을 깨고 몸을 일으켰다는 소식에는 무림인 중 그 누구도 놀라지 않았다.

엄연히 중원에 속한 그들의 시선에서, 포달랍궁은 아득한 과거부터 사악한 교리를 따르는 사이비(似而非)에 불과한 존재들.

이미 신 무림맹 창설 이후부터 여러 차례 사자를 보내어 동맹을 청했음에도, 늘 묵묵부답으로 일관해 왔던 그들이 지금 같은 상황에 나선다는 것은 한 가지 사실만을 뜻했다.

“……암천, 또다시 놈들이군.”

하지만 다행히도 사천에는 강력한 지원군이 있었다.

언제나 그렇듯이 중도(中道)를 지키고 있는 북해빙궁과 달리, 한 청년의 놀라운 활약으로 내전의 위기를 극복하고 무림맹과 동맹을 결의한 남만야수궁이.

그렇기에 세간의 이목은 장강수로맹과 녹림맹의 움직임을 향해 집중되었다.

처음 진실을 접하고 충격에 휩싸인 것도 잠시, 이제는 이런 흑도들의 준동을 비웃는 목소리들도 적지 않았다.

“제아무리 한 차례 대승을 거두었다고는 하나, 흑도는 흑도. 달라지는 것은 없다.”

그리 틀린 말은 아니었다.

장강수로맹과 녹림맹 산하의 총 전력이 이만에 가까울 정도라고는 하나, 단순히 머릿수만으로 모든 것을 가질 수 있다면 천하 무림은 개방의 것이었을 테니까.

무림맹을 중심으로 완전히 결집한 정파 무림의 전력은, 고작 이 정도로 흔들리지 않을 것이라는 확신이 모두에게 있었다.

“섬서에는 화산과 종남, 호북에는 무당과 제갈세가가 있소. 더불어 천자 휘하의 금군(禁軍)이 나선다면 놈들은 암천과 손잡은 것을 후회하게 될 거요.”

그러나 이 예측에는 몇 가지의 치명적인 오류가 있었다.

첫째는 본산에 남아 있는 종남파의 전력이 극히 미미했다는 것이었고.

둘째는 수십여 만에 달하는 금군 중 대부분이 천자가 머무르는 황도(皇都)가 위치한 강소성에 집중되어 있다는 것이었으며.

마지막 셋째는, 모습을 감출 생각도 없이 훤한 대낮에 거침없이 서쪽을 향해 나아가는 녹림맹과 장강수로맹의 군세가 생각 이상으로 거대하다는 사실이었다.

마치, 눈 덮인 비탈길을 따라 서서히 크기를 불려가는 눈덩이처럼.

“호북에 결집해 있던 녹림도들이 반 시진 전 통산(通山)을 넘었답니다! 현재까지 추정된 머릿수는 약 오천!”

“오천이라니, 그 무슨……!”

“반나절 전만 하더라도 삼천 남짓이라고 하지 않았나!”

“그, 그것이. 아마 각 산채에 흩어져 있던 병력들이 합류한 것 같습니다.”

“말도 안 되는 소리!”

하지만 전령이 가져온 소식을 강력히 부정하던 그들은 곧 알게 되었다.

이미 감숙성에서의 대전투가 벌어지기도 전, 은밀하게 호북과 섬서 일대를 중심으로 결집한 두 집단의 도적들에게 또 다른 지원군이 합류했음을.

그것도 중원 무림이 가장 경계하고 있던 모종의 수단을 통해서.

“……빌어먹을, 놈들이 바로 그 저주받을 사술(邪術)을 쓴 것이 틀림없소.”

“사술이라면. 설마?”

“맞소. 이동진(移動陳)이오.”

처음에는 철저한 보안으로 틀어막았던 이동진의 존재는, 이제 더 이상 극소수만의 비밀이 아니었다.

사람에게 눈과 귀가 있는 한, 언제고 비밀은 새어 나가는 법.

무림맹 수뇌부와 천면호리 송호가 이끄는 은영각이 전면에 나섰지만, 어째서인지 이동진에 관한 비밀은 알려졌고 오늘날에 이르러 마침내 그 실체를 확인한 문주와 가주들은 서늘한 한기를 느꼈다.

‘쳐야 한다. 지금 바로.’

장강수로맹과 녹림맹은 어디까지나 저마다의 연합체다.

적게는 수십, 많게는 수백에서 일천까지의 수하를 거느린 채주들이 각자의 맹주에게 충성을 바치고 명령에 따라 집결과 해산을 반복한다.

따라서 놈들을 칠 수 있는 가장 좋은 적기는 바로 지금이었다.

아직 적들이 완전히 결집하지 않았을 때. 한자리에 모여 강력한 군집체를 이루지 않았을 때.

하지만 기어코 모두가 내심 우려했던 변수가 발생하고야 말았다.

도무지 어딘가에 있는지조차 모르는 이동진과 이를 통해 흑도들에게 합류하고 있는 암천의 강력한 전력이었다.

‘만약, 지금 놈들과 맞선다면?’

위험하다.

이동진의 존재 자체도 엄청난 위협이지만, 전투에서 승리할 수 있으리라는 보장이 없다.

당장 무림의 태산북두인 소림이, 치명적인 독과 암기로 오대세가의 일익을 차지한 사천당문이, 그리고 새외의 남만야수궁과 하북팽가마저 극심한 피해를 입었으니까.

그뿐인가. 알려진 바에 의하면 공동과 종남 역시 감숙에서 엄청난 타격을 입었다고 했다.

누구도 기억하기 싫은 정마대전 당시와 비견해도 절대 뒤떨어지지 않을 정도의, 아니 그 이상의 타격을.

구파일방과 오대세가.

천하 무림을 지탱하는 열다섯 그루의 거목(巨木)들마저 암천이라는 먹구름이 일으킨 태풍 앞에 뿌리가 흔들리고 있는 현재, 자신이 가진 모든 것을 걸고 위험과 직면할 용기를 내는 것은 결코 쉬운 일이 아니었다.

혈혈단신이 아닌, 식솔들의 목숨을 책임져야 하는 문주와 가주들에게는 더더욱.

“나는…… 포기하겠소.”

“석 대협! 그게 무슨 말이오!”

“냉정하게 봅시다. 지금 이 자리에 모인 우리의 전력만으로 놈들에게 맞설 수 있다고 생각하시오?”

“그건!”

“그대도 알고 있지 않소. 결과는 정해져 있다는 것을. 지금은 조금이라도 힘을 아껴야 할 때요. 다행히 암천과 손을 잡은 저 배신자들은 오직 서쪽으로만 향하고 있으니, 당장의 충돌은 피할 수 있을 거요.”

“다행? 지금 다행이라고 했소? 놈들이 무엇을 노리는지 정녕 모르고 하는 소리요?”

“알고 있소. 중원의 지원군을 옴짝달싹하지 못하게 만들고 청해성을 완전히 손아귀에 넣는 것. 그게 놈들의 목적일 테지.”

“그걸 알고 있으면서도……!”

“하지만 이번만큼은 어쩔 수 없소. 나는 초절정 고수도, 구파일방의 문주도 아니니. 미안하오.”

“석 대협!”

“부디 대협이라 부르지 마시오. 내게는 그럴 만한 자격이 없소. 그저 식솔들의 안위만 챙기고자 하는 비겁한 문주일 뿐이지.”

씁쓸하게 뇌까린 그가 자리를 뜨자, 침잠한 얼굴로 고개를 떨구고 있던 몇몇 문주들도 그를 따라 일어났다.

그리고 상석(上席)에 앉아, 조용히 그 광경을 바라보던 청수한 인상의 중년인 역시도.

드륵.

배신감과 분노, 더불어 마음 한구석에 존재하는 공감으로 복잡한 표정을 짓고 있던 이들은 중년인의 그런 모습에 눈을 부릅떴다.

설령 이곳에 있는 모두가 자리를 뜰지라도, 그만큼은 아닐 거라 굳게 믿고 있었으니까.

“가, 가주(家主)!”

“이게 무슨!”

하지만 그들의 불길한 짐작과 달리, 중년인은 담담한 얼굴로 어깨를 으쓱해 보일 뿐이었다.

“아, 오해하지 말게. 잠시 바람이나 쐬고 올 테니까.”

사람들은 안도했지만, 동시에 한숨을 내쉬었다.

호북 무림의 영수 중 삼분지 일이 빠져나간 상황에서 바람이나 쐬고 온다니.

실로 그 다운 말이었지만, 어처구니없기는 매한가지였다.

“하필이면 지금 말입니까?”

“그렇네. 지금.”

“논의할 사항이 너무 많습니다. 당장 무림맹에서도 제대로 된 결단을 내리지 않고 있…….”

“정 급하다니 알겠네. 그럼 여기서 싸지, 뭐.”

“예?”

어리둥절해하는 사람들을 향해, 중년인이 심각한 표정으로 바지춤을 움켜잡았다.

“방광이 터질 것 같네.”

“……!”

“이제 나이를 먹어서 그런지, 아니면 한참 동안 본가를 벗어나 바깥 생활을 오래 해서인지는 몰라도 오줌보가 약해진 모양일세. 게다가 그저 가만히 앉아 있기만 해도 엉덩이의 은밀한 부위가 저릿저릿한 것이…….”

주절주절 말을 이어가던 중년인이 사람들의 표정을 보고 입맛을 다셨다.

“이것 참, 내가 괜한 얘기를 했군. 앞서 하던 얘기나 계속하세.”

“……그냥 다녀오십시오.”

“아니긴 뭘. 그냥 여기에서 지리겠네. 제갈무후(諸葛武侯)께서도 한창 바쁠 때는 그러셨을 거야.”

“다녀오십시오. 제발.”

“어라, 그럼 그래도 되겠나?”

“예. 부디 저희를 위해서라도.”

“자네들이 이토록 간절하게 세 번이나 청하니, 삼고초려(三顧草廬)의 고사를 따라야겠구먼.”

반쯤 체념한 사람들을 보며 빙긋 웃은 중년인, 아니 제갈세가의 가주인 와룡객(臥龍客) 제갈풍은 후다닥 자리를 벗어났다.

그리고 측간이 아닌 미로처럼 얽힌 길을 지나길 한참, 가주에게만 허락된 내당의 화원에 이르러 비로소 발걸음을 멈추었다.

“눈에 띄지 않게 머무르시는 건 좋지만, 그래도 어디에 계실지 정도는 알려주셔야지요.”

넓은 화원의 한구석.

과거 제갈공명이 손수 심었다는 뽕나무밭을 바라보고 있던 누군가의 뒷모습을 향해, 제갈풍이 나직이 덧붙였다.

“안 그렇습니까? 맹주(盟主).”
```

## Final English reading copy

```markdown
# Chapter 1085

The rumors spread in an instant.

From mouth to mouth.

On the beating wings of messenger pigeons.

Along with the hooves of horses racing across mountains and fields under the crack of whips, and the smoke of beacon fires staining the sky gray.

Before the people shaken by the astonishing news could even determine whether it was true, they saw it with their own eyes.

Countless ships cutting swiftly through the river, their flags billowing proudly in the favorable wind.

The Yangtze River Channel League.

The moment they made out the five characters written on the flags, swollen full by the wind, they realized that denying it any longer would be no different from escaping reality.

Everything they had seen and heard was no baseless rumor.

It was true.

A mere band of river pirates, who had lived parasitically on the Yangtze with the world’s tacit consent, had at last risen to become its true rulers.

And they had done it against the Great Nation itself—the master of the world.

“…Gods of heaven and earth.”

The groan that slipped between someone’s lips was hollow.

After all, this vast empire, founded under the Mandate of Heaven, was collapsing.

No—their heaven was.

“If this isn’t defying heaven, then what is?”

More than a hundred years had passed since the age of warring heroes came to an end and a unified dynasty was born.

The country folk, who had held the Great Nation ruled by the Son of Heaven up as the heavens themselves, trembled with unease. The Confucian scholars groaned as they realized that the natural order had crumbled. The betrayed martial artists were swept up in anger and shock.

“Those bandits finally…!”

“I knew something was off. We should never have trusted dark-path figures in the first place!”

But the Yangtze River Channel League’s betrayal wasn’t the only news to shock everyone.

“Two days ago, the Green Forest bandits rebelled in Hubei and Shaanxi!”

The Green Forest Alliance, which divided the world’s dark-path forces with the Yangtze River Channel League, had risen up.

And on top of that, people belatedly realized that storm clouds were gathering beyond the distant Great Wall.

“An urgent report from Sichuan! Potala Palace in Tibet is on the move!”

Potala Palace.

The news that the esoteric monks—counted among the Three Outer Powers alongside the North Sea Ice Palace and Nanman Beast Palace—had finally broken their long silence and stirred to action surprised no one in the Murim.

In their eyes, as people of the Central Plains, Potala Palace had been nothing more than a pseudo-religion following evil doctrines since the distant past.

The New Murim Alliance had sent envoys to seek an alliance several times since its founding, but Potala Palace had always answered with silence. For them to act now, in a situation like this, could only mean one thing.

“...Dark Heaven. It’s them again.”

Fortunately, Sichuan had powerful reinforcements.

Unlike the North Sea Ice Palace, which—as always—remained neutral, Nanman Beast Palace had overcome the threat of civil war thanks to the astonishing exploits of a young man and resolved to ally itself with the Murim Alliance.

So the world’s attention focused on the Yangtze River Channel League and the Green Forest Alliance.

The initial shock of learning the truth soon passed, and quite a few voices began to scoff at the dark-path forces’ uprising.

“Even if they won one great victory, dark-path figures are still dark-path figures. Nothing’s changed.”

It wasn’t entirely wrong.

The Yangtze River Channel League and the Green Forest Alliance together had nearly twenty thousand men, but if numbers alone could claim everything, the Beggars’ Sect would own the Murim world.

Everyone was confident that the orthodox factions, now completely united around the Murim Alliance, wouldn’t be shaken by a force this small.

“Shaanxi has Huashan and Zhongnan, and Hubei has Wudang and the Zhuge Clan. And if the Imperial Army under the Son of Heaven moves out, those bastards will regret joining hands with Dark Heaven.”

But this prediction had a few fatal flaws.

First, the Zhongnan Sect had very few forces left at its headquarters.

Second, most of the hundreds of thousands of Imperial Army troops were concentrated in Jiangsu, where the Imperial Capital—home of the Son of Heaven—was located.

And third, the Green Forest Alliance and the Yangtze River Channel League were marching west in broad daylight, with no thought of hiding themselves, and their forces were far larger than anyone had expected.

Like a snowball slowly growing as it rolled down a snow-covered slope.

“The Green Forest bandits gathered in Hubei crossed Tongsan half a shichen ago! Their numbers are estimated at around five thousand!”

“Five thousand? What in the—”

“Didn’t you say they were only around three thousand at most half a day ago?”

“W-Well, it seems the forces scattered among the various strongholds have joined them.”

“That’s absurd!”

But the men who had so forcefully denied the messenger’s report soon learned the truth.

Another force had joined the two bands of outlaws who had secretly gathered around Hubei and Shaanxi even before the great battle in Gansu.

And they had done so by means of a certain method the Central Plains Murim had been most wary of.

“...Damn it. They must have used that accursed dark art.”

“Dark art? Don’t tell me…”

“That’s right. A Moving Formation.”

The existence of the Moving Formation, once kept under the tightest security, was no longer a secret known only to a tiny handful.

As long as people had eyes and ears, secrets would always find a way to leak.

The Murim Alliance leadership and the Hidden Shadow Pavilion, led by the Thousand-Faced Fox Song Ho, had taken the field, but for some reason, the secret of the Moving Formation had still gotten out. Now that they’d finally seen it for themselves, the Sect Leaders and Family Heads felt a chill.

*We have to strike. Right now.*

The Yangtze River Channel League and the Green Forest Alliance were, after all, coalitions of separate groups.

Their Stronghold Lords commanded anywhere from a few dozen to several hundred, or even a thousand, men each. They pledged loyalty to their respective alliance leaders and repeatedly gathered and dispersed at their command.

So the best time to strike them was right now.

Before the enemy had fully assembled. Before they had gathered in one place and formed a powerful force.

But the variable everyone had secretly feared had finally come to pass.

No one knew where the Moving Formations were. And through them, Dark Heaven’s powerful forces were joining the dark-path figures.

*What if we fight them now?*

It was dangerous.

The Moving Formations themselves posed an enormous threat, and there was no guarantee they could win the battle.

Shaolin, the Mount Tai and Northern Dipper of the Murim. The Sichuan Tang Clan, one of the Five Great Families, with its deadly poisons and hidden weapons. Nanman Beast Palace and even the Hebei Peng Family had all suffered terrible losses.

That wasn’t all. According to reports, the Kongtong and Zhongnan Sects had also been hit hard in Gansu.

The damage was no less severe than during the Great Faction War, a time no one wanted to remember. If anything, it was worse.

The Nine Sects and One Gang. The Five Great Families.

With even the fifteen great trees supporting the Murim world trembling at their roots in the typhoon stirred up by Dark Heaven’s storm clouds, it was no easy thing to summon the courage to risk everything and face the danger.

Especially for Sect Leaders and Family Heads, who were responsible for the lives of their families—not just their own.

“I… I give up.”

“Sir Seok! What are you saying?”

“Let’s be realistic. Do you think the forces gathered here can stand against them?”

“But—”

“You know it too, don’t you? The outcome is already decided. We have to conserve what strength we can. Fortunately, those traitors who joined hands with Dark Heaven are heading only west. We can avoid a clash for now.”

“Fortunately? Did you just say ‘fortunately’? Do you really not know what they’re after?”

“I know. They want to pin down the reinforcements from the Central Plains and take Qinghai completely into their grasp. That must be their goal.”

“And you know that, yet…”

“But this time, I have no choice. I’m no Supreme Peak master, nor am I a Sect Leader of one of the Nine Sects and One Gang. I’m sorry.”

“Sir Seok!”

“Please don’t call me that. I’m not worthy of it. I’m just a cowardly Sect Leader who wants to protect his family.”

After muttering bitterly, he left. Several other Sect Leaders, their faces downcast, got up and followed him.

And so did the middle-aged man sitting quietly in the seat of honor, watching them.

Scrape.

The others wore complicated expressions—betrayal and anger, mixed with a sympathy that lingered in one corner of their hearts. At the sight of the middle-aged man getting up, their eyes widened.

They had firmly believed that even if everyone else left, he wouldn’t.

“F-Family Head!”

“What is this?”

But contrary to their ominous suspicions, the middle-aged man merely shrugged, his expression calm.

“Ah, don’t misunderstand. I’m just going to get some air.”

The others relaxed, but let out a sigh at the same time.

A third of Hubei Murim’s leading figures had left. And he was going to get some air.

It was certainly like him, but it was no less ridiculous.

“Why now, of all times?”

“Yes. Right now.”

“There’s so much to discuss. Even the Murim Alliance hasn’t made a proper decision yet…”

“If it’s that urgent, I’ll just piss right here.”

“Pardon?”

As the others stared at him in bewilderment, the middle-aged man clutched the front of his trousers, looking grave.

“My bladder’s about to burst.”

“...!”

“I don’t know if it’s because I’m getting old, or because I’ve spent so long away from our family, living out in the world, but I think my bladder’s gotten weak. And on top of that, even when I’m just sitting still, a certain private spot on my backside starts tingling…”

The middle-aged man rambled on, then saw their expressions and smacked his lips.

“Goodness, I shouldn’t have brought that up. Let’s continue where we left off.”

“...Just go.”

“No need. I’ll just wet myself right here. I’m sure even Zhuge Wuhou did the same when he was busy.”

“Please go. We’re begging you.”

“Oh? Then it’s all right if I do?”

“Yes. For our sake, please.”

“Since you’ve begged me so earnestly three times, I suppose I’ll have to follow the story of the Three Visits to the Thatched Cottage.”

The middle-aged man smiled at the half-resigned group. Then, Zhuge Feng, Family Head of the Zhuge Clan—or rather, the Crouching Dragon Guest—hurriedly left.

He didn’t head for the privy. He walked for a long while through winding paths like a maze, until he reached the garden in the Inner Hall, a place only the Family Head was permitted to enter. At last, he stopped.

“It’s all well and good to stay out of sight, but you should at least let me know where you’ll be.”

In a corner of the spacious garden, someone stood with their back to him, gazing at a mulberry grove said to have been planted by Zhuge Kongming himself.

Zhuge Feng addressed the figure in a low voice.

“Don’t you agree, Alliance Leader?”
```

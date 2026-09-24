<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1006.txt",
      "sha256": "2ae7c757015cd196b0215ee65bd3c2fef936ad1ab0291846dcea1056aef12c29",
      "bytes": 12794
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "76aec9fe74341b5bcbeb117a57082ac378fa3dd539dd923330b4f690e9899a0c",
      "bytes": 663
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a2ba2080787f93b9df4a81c1f6c7b6f602a1beff6efab59540e4d4c1fd5ee248",
      "bytes": 237214
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "214d201f8a3430e6f12a06d5b40d4246862a247bf9ed32cc473f40993ab88c4c",
      "bytes": 1408
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "9efafde3f282a8f5970a541e77b203a21e66a3b35305d36c1cb9f8fd700e1539",
      "bytes": 937
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "bb5888ae68e83b262deaa979993f2c2fbd1f581820c70d14e2e84912c67b362f",
      "bytes": 733
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "067729a2c21d0cebd6add3028ac0a1a91cfffc88528277258b279acb6a4401bb",
      "bytes": 275591
    }
  ],
  "estimated_tokens": 9745
}
-->

# Durable State Update — Chapter 1006

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
1 and safe_through 1006. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1006. Profile updates may replace only one
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
  "chapter": 1006,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1006,
    "continuity_sources": [1006],
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
    "After four days of hard travel, the Fire Dragon Pavilion members are resting over a feast.",
    "Song Ilseom asserts his seniority over Hyuk Mujin, who protests Song's casual speech but continues to address him politely.",
    "Taishan is unusually motionless and not eating despite the feast; Namho reacts to a scent that recalls a recent memory."
  ],
  "continuity_sources": [
    1005
  ],
  "open_questions": [
    "Why has Taishan stopped eating, and what has caught Namho's attention?",
    "Why did Sama Pyo's eyes sink as his father approached?"
  ],
  "safe_through": 1005,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 항산검문   | **Mount Heng Sword Sect**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 산서     | **Shanxi**             |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 곤륜     | **Kunlun**             |
| 팔천협    | **Eight Spring Gorge** |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 상호 | **Sangho** | Go Se-won's young son. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |

## Listed compact profiles

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1005
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1005
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1004
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating, yet outwardly gentle; he uses persuasive sophistry and a calming manner to justify hard choices.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

## Korean source

```text
＃1006화



촤르륵.

두툼한 짐승의 가죽이 커다란 탁자를 뒤덮는다.

사람의 손길을 거쳐 무두질 된 가죽의 표면에는 각각의 지형을 묘사한 그림과 글자로 빼곡하게 채워져 있었다.

“보시는 바와 같이 이건 본문에서 제작한 지도요. 오랜 세월에 걸쳐 감숙(甘肅)의 모든 지형지물을 상세히 기록, 변동된 부분까지 일일이 수정하며 완성했지.”

지도에 대해 설명하는 사마공의 목소리는 담담했지만, 이 자리에 모인 수뇌부들 중 저 지도가 의미하는 바를 모르는 이는 없었다.

말이 쉬워 성(省)이지, 천하의 크고 작은 조각이나 다름없는 각 성의 면적은 아무리 작더라도 한 나라에 버금간다.

그렇다고 드론이 있나, 인공위성이 있길 하나.

당장의 현실이 이러니 지도를 제작하기 위해서는 엄청난 재물과 인적 자원이 필요한 것은 당연지사.

그럼에도 이토록 거대하고 상세한 지도를 제작할 수 있다는 것은, 사마공이 이끄는 흑룡마문(黑龍魔門)이 감숙 일대에서 어느 정도의 장악력을 지녔는지 알 수 있는 부분이었다.

더불어 사마공이 가진 정보력도 함께.

“공깨나 들였겠군. 그래서, 이 근방은 네놈이 꽉 잡고 있다고 자랑이라도 하고 싶은 게냐?”

우회하는 방법 따위는 모르는 적천강의 직진 화법에, 사마공의 입가에 엷은 미소가 맺혔다.

“그럴 리 있겠습니까. 중원의 대들보 중 하나인 공동파가 있는데 저희가 어찌 감히.”

어투는 겸손하지만 사마공과 흑룡마문이 감숙성에서 어느 정도의 입지를 지녔는지 모르는 사람은 없다.

게다가…….

“중요한 회의인데, 바로 그 대들보가 빠져 있네요.”

맞다.

정작 지금 이 자리에는 공동파가 빠져 있다.

그러나 정곡을 찌르는 내 한마디에도, 사마공의 입가에 맺힌 미소는 여전했다.

“괜한 걱정할 필요 없네. 대들보는 지금 다른 곳에서 곧 쏟아질 폭우를 막기 위해 준비 중이니까.”

“공동파가 이미 전선(戰線)에 투입되었다는 뜻이구려.”

불쑥 끼어든 풍운검군을 향해 사마공이 고개를 끄덕였다.

“장문인의 짐작대로요. 돈황(敦煌)과 대설산(大雪山), 그리고 기련산(甘肅省)에 걸쳐 삼중에 달하는 전선을 구축해 놓았소.”

“삼중이라, 병력이 너무 분산된 것 아니오?”

풍운검군의 우려에 회의실 안의 사람들이 동의한다는 듯 고개를 끄덕였다.

만약 암천의 대군이 이곳 감숙으로 진군한다면, 단 한 번의 싸움으로 운명이 갈릴 대전투가 벌어질 테니까.

하지만 주위의 그런 반응에도 사마공의 안색은 변함이 없었다.

“비록 곤륜(崑崙)만큼은 아니나, 대설산과 기련산 역시 천하에서 열 손가락 안에 드는 험산. 게다가 적들에게는 이동진이라 불리는 기괴한 사술이 있으니, 돈황에 모든 전력을 집중시키는 건 너무 위험하다고 판단했소.”

“사마 문주의 의견에는 빈도 역시 동의하오만, 문제는 세 개나 되는 전선을 유지할 만한 전력이 있냐는 거요.”

사실상 수적열세야말로 가장 큰 걸림돌이다.

적들은 물경 십만을 아우르는 대군세.

설령 놈들이 병력을 분산시켜 세 개의 성을 동시에 노린다고 하더라도, 단순 계산으로 따져도 삼만이 넘는 머릿수가 개떼처럼 몰려올 것이다.

‘그 많은 적을 상대하기 위해서는 한곳에 집결해야 한다. 그것도 최대한 지형지물을 이용해서 싸워야만 승산이 있어.’

실제로 얼마 전 산서성에서 벌어진 전투가 그러했고, 행운과 투지가 겹쳐 승리를 얻어냈다.

그리고 이는 굳이 군사 전략에 조예가 없더라도 누구나 아는 사실.

그런데 일개 촌부도 아닌, 흑룡마문이라는 거대 방파를 일구어낸 흑야왕 사마공이 그런 기본적인 상식도 모를까?

‘말도 안 되지.’

나는 담담하게 사람들의 시선을 받아내는 사마공의 모습에서, 보이지 않는 자신감을 읽어 냈다.

“이미 충분하군요. 감숙의 전력은.”

그 순간, 사마공의 입가에 걸린 미소가 한층 짙어졌다.

“달포 전, 감숙 무림 전체에 비상을 내렸네. 본문과 공동파는 물론, 일대의 모든 무림 방파가 주위를 경계한 지 오래였던지라 금세 병력을 끌어모을 수 있었지.”

“그렇다는 건…….”

“삼만. 지금까지 결집한 병력일세. 감숙 무림의 모든 역량을 총동원했지.”

“……!”

“……!”

수뇌부들의 눈이 부릅떠졌고, 이는 나 역시 크게 다르지 않았다.

‘삼만이라니.’

실로 어마어마한 대병력이다.

지난날 팔천협을 틀어막고 대초원의 군세와 맞섰던 산서성의 병력이 만오천에 불과했다는 사실을 생각한다면 더더욱 그랬다.

심지어 사마공이 ‘감숙 무림’이라는 사족을 덧붙였다는 것은, 저 삼만이라는 머릿수가 전부 무림인으로 이루어져 있다는 것을 뜻했다.

총병력의 절반 이상이 관병으로 구성되었던 산서성 때와는 비교도 할 수 없는 전력.

물론 항산검문과의 분쟁에 이어 대장로의 배신으로 이미 한차례 극심한 피해를 입었던 산서 무림이지만, 그것까지 감안하더라도 삼만이라는 대병력은 언강생심이나 다름없다.

“도, 도대체 그 많은 병력을 어디에서……?”

아마도 이 자리의 모두가 품었을 의문을 대신하여 풍운검군이 말을 꺼낸 그때, 눈살을 찌푸린 채 상황을 지켜보던 적천강이 문득 입을 열었다.

“사파(邪派) 놈들은 머릿수 빼면 시체지. 그렇지 않느냐?”

사마공이 빙긋 웃으며 고개를 끄덕였다.

“부정하지는 않겠습니다.”

“하나, 아무리 그렇다 한들 삼만이라는 머릿수는 설령 중원(中原)의 구파일방이라 할지라도 불가능에 가까울 터.”

“그 또한 맞지요. 언제 허리춤에 찬 칼을 거꾸로 휘두를지 모르는 파락호들이 이리 많다면, 대국(大國)에서 가만히 두고 보았겠습니까.”

비록 천자가 암천을 역적으로 규정한 이후부터 유명무실해진 표현이긴 하지만, 관무불가침(官武不可侵)이라는 말이 괜히 생긴 것이 아니다.

이는 무림의 탄생과 함께 자연스럽게 맺어진 암묵적인 규칙이다.

모난 돌은 언제고 반드시 정을 맞게 되는 법.

광활한 천하 곳곳에 존재하는 수많은 무림 방파는 충돌을 피하기 위해 상호간의 견제와 합의를 반복해 왔고, 대국은 나라의 근간이 위협되지 않는다는 전제하에 그들의 존재를 묵인해 주었다.

오죽하면 왕조(王朝)가 바뀌어도 무림(武林)은 남아 있다는 말이 나왔겠나.

그런데 현재의 감숙 무림은 바로 그 암묵적인 규칙을 넘어섰다.

중원도 아닌 변방에서 삼만을 아우르는 무림인들을 결집시켰고, 이는 감숙성의 모든 무림 방파를 뒤집어 탈탈 털어도 나올 수 없는 대병력이었다.

‘그렇다는 건.’

남은 건 하나밖에 없다.

대부분이 어느 특정한 문파에 적(籍)을 두지 않은 채, 오직 필요와 이익을 좇아 움직이는 인간군상들.

“흑도(黑徒)까지 긁어 모으다니, 어지간히 급했던 모양이로군.”

흑도.

아득한 세월 동안 불편한 공존을 이어 가고 있던 그들의 정체에 몇몇 사람들, 특히 풍운검군의 눈빛이 침잠하게 가라앉았다.

“사마 문주. 적 대협께서 하신 말씀이 사실이오?”

사마공이 침착하게 대꾸했다.

“그들 중 일부가 흑도인 것은 맞소만, 혹여 무슨 문제라도?”

“……그건.”

“인정하리다. 본인은 부정할 수 없는 사파인이오. 장강수로맹과 녹림맹 또한 뿌리부터 흑도지. 아, 저기 있는 내 아들놈 역시 마찬가지올시다.”

갑작스러운 아버지의 지목에, 줄곧 침묵하고 있던 사마표의 눈빛이 흔들렸다.

그러나 그것도 잠시, 재차 흘러나오는 사마공의 목소리에 사람들의 시선은 금세 제자리로 돌아갈 수밖에 없었다.

“그리고 앞서 언급한 모두에게는 한 가지 공통점이 있지. 무엇인지 아시오?”

안다. 이 자리의 모두가.

하지만 사람들은 무거운 얼굴로 침묵을 지켰다.

단 한 사람만 빼고.

“무림맹을 위해 싸웠고, 또한 무림맹을 위해 싸우고 있지.”

적천강이다.

화왕(火王)이라는 별호를 증명하듯, 불그스름하게 달아오른 그의 눈동자에 사마공의 모습이 비쳤다.

“사파건, 흑도건. 어디서 굴러먹다 왔는지 모를 개뼉다귀 건  아무래도 상관없다. 그것들의 손에 들린 병장기가 암천을 향하고 있다면야.”

사마공이 굳은 얼굴로 고개를 끄덕였다.

“과거에도 그랬듯이, 이번 또한 필시 그럴 것입니다.”

“네 녀석을 의심하는 것이 아니다. 이런 변방까지 흘러들어올 정도의 흑도라면 어지간히 썩어빠진 놈들일 터. 만에 하나 불상사가 일어난다면…….”

“제 목을 걸지요.”

그때였다.

말없이 사마공을 응시하던 적천강이, 불현듯 고개를 돌려 좌중을 쓸어본 것은.

“너희의 의중은 어떠하냐?”

지금 이 자리에는 사마공과 함께 우리를 마중 나온 감숙 무림의 명숙(名宿)들이 있었지만, 적천강의 물음은 그들을 향한 것이 아니었다.

우리와 함께 온 종남파의 중진들.

그들 중 중심에 선 풍운검군이 답을 망설이는 사이, 그의 사형들인 노호검객과 태을무정검이 차례대로 입을 열었다.

“누가 그러더군요. 하얀 고양이든, 검은 고양이든 쥐만 잘 잡으면 그만이라고.”

“빈도가 아는 사마 문주는 사파인이기 이전에 함께 전란을 헤쳐 나온 전우이자 협객(俠客)입니다. 그런 이가 목숨까지 걸었으니, 이것이야말로 실로 통탄할 노릇이 아니겠습니까.”

마치 기다렸다는 듯 청산유수로 말을 쏟아내는 두 노도사의 모습을 바라보던 그때, 적천강의 시선이 문득 이쪽을 향해 움직였다.

“그래서, 꿀은 다 처먹었느냐?”

왜 꿀 먹은 벙어리 행세를 하고 있냐는 그의 물음에, 나는 짐짓 입맛을 다시며 대답했다.

“예, 뭐. 달달하던데요.”

“귀한 꿀을 그리 오랫동안 머금고 있었으니, 이제 할 말이 있을 터.”

“제가 결정할 수 있는 부분입니까?”

“어림도 없지. 네깟놈이 뭐라고.”

실소를 흘린 나는 천천히 주위를 둘러보았다.

이름도, 별호도 잘 모르는 낯선 얼굴들이 대부분이다.

흑룡마문의 중진들과 저마다 크고 작은 방파를 이끄는 감숙 무림의 영수(領袖)들.

그 중심에 사마공이 있었다.

“몇 가지만 여쭤봐도 되겠습니까?”

“뭐든지.”

“이 모든 것을 문주께서 홀로 결정하셨다고는 생각되지 않는데. 맞습니까?”

“당연한 말을. 이 자리에 계신 여러 문주들과 공동파 또한 동의했네.”

“그럼 만약 암천이 노리는 것이 감숙이 아니라면…….”

“일부 병력을 남겨놓고 즉각 청해로 향할 걸세. 하지만 그럴 일은 벌어지지 않겠지.”

“어째서입니까?”

“조짐이 심상치 않네. 마교에서 암천이 되었을 뿐, 우리에게 있어 사막 너머의 적들은 늘 가장 큰 경계 대상이었고 이는 정마대전 이후에도 마찬가지였지.”

“조짐이라면.”

“아직 확실치 않아 당장 입에 담을 수는 없네. 이미 믿을 만한 이들을 선별하여 사막 너머로 정찰을 보냈으니 돌아오면 확실해지겠지. 그러니…….”

사마공의 시선이 나에게서 적천강을 향해 움직였다.

“감숙의 방비는 저희에게 맡기시고, 노선배께서는 청해로 가시는 것이 좋지 않을까 합니다. 비록 화산파를 비롯한 지원군이 있다 하더라도, 당장 시급을 다투는 쪽은 아무래도 청해성이 아니겠습니까.”

“청해, 청해라.”

적천강이 신음하듯 낮게 읊조린 그 순간이었다.

“무, 문주님!”

굳게 닫힌 문틈 사이로, 다급한 목소리가 울려 퍼진 것은.
```

## Final English reading copy

```markdown
# Chapter 1006

Rrrrip.

A thick animal hide unfurled across the large table.

Its surface had been tanned by human hands and covered edge to edge with drawings and writing that depicted the terrain in detail.

“As you can see, this map was made by our sect. We’ve spent many years documenting every feature of Gansu in detail, revising each change as it occurred, until it was complete.”

Sima Gong’s voice was calm as he explained the map. But none of the leaders gathered here failed to understand what it meant.

A province might sound small, but each one was practically a nation of its own—a great or small piece of the world. Even the smallest was comparable in area to a country.

And it wasn’t as if they had drones or satellites.

Given the reality of the time, producing a map required enormous wealth and manpower. That much was only natural.

And yet the fact that they could make a map this vast and detailed showed just how much control the Black Dragon Demon Gate, led by Sima Gong, held across Gansu.

It also spoke to the reach of Sima Gong’s intelligence network.

“You must’ve spent a fortune on it. So what, do you want to brag that you’ve got this area locked down?”

At Jeok Cheongang’s blunt way of speaking, which knew nothing of beating around the bush, a faint smile appeared on Sima Gong’s lips.

“How could you think that? The Kongtong Sect is one of the pillars of the Central Plains. How could we dare?”

His words were humble, but no one was unaware of the position Sima Gong and the Black Dragon Demon Gate held in Gansu Province.

And besides…

“This is an important meeting, but that very pillar is missing.”

That was right.

The Kongtong Sect was absent from this gathering.

But even after I’d struck right at the heart of the matter, Sima Gong’s faint smile didn’t waver.

“No need to worry over that. The pillar is preparing elsewhere to hold back the torrential rain that’s about to pour down.”

“So the Kongtong Sect has already been sent to the front lines.”

Sima Gong nodded at the Wind-and-Cloud Sword Lord, who’d cut in without warning.

“Just as the Sect Leader guessed. We’ve established three lines of defense stretching across Dunhuang, the Great Snow Mountain, and the Qilian Mountains in Gansu Province.”

“Three lines? Isn’t that spreading our forces too thin?”

The people in the conference room nodded as if they shared the Wind-and-Cloud Sword Lord’s concern.

If Dark Heaven’s vast army marched into Gansu, a great battle would decide everything in a single clash.

But even in the face of everyone’s reaction, Sima Gong’s expression remained unchanged.

“Though they’re no match for Kunlun, the Great Snow Mountain and the Qilian Mountains are among the ten most treacherous mountain ranges under heaven. And our enemies have a bizarre form of dark arts they call a Moving Formation. We judged that concentrating all our forces in Dunhuang would be too dangerous.”

“I agree with Sect Leader Sima’s opinion. But the question is whether we have enough forces to hold three fronts.”

The greatest obstacle, in the end, was that we were outnumbered.

The enemy army numbered a staggering hundred thousand.

Even if they split their forces and attacked three provinces at once, a simple calculation meant more than thirty thousand of them would come rushing in like a pack of dogs.

*To face that many enemies, we need to gather in one place. And we’ll only have a chance if we make the best possible use of the terrain.*

That was what had happened in the battle in Shanxi Province not long ago. Luck and determination had come together to win us the day.

And this was common sense, even for someone with no knowledge of military strategy.

But would the Black Night King Sima Gong, who’d built the massive Black Dragon Demon Gate from the ground up, really not know something so basic?

*No way.*

I read a quiet confidence in Sima Gong as he calmly met everyone’s gaze.

“That should be more than enough. Gansu’s forces.”

At that, the smile on Sima Gong’s lips deepened.

“About a month ago, I put all of Gansu Murim on alert. Our sect and the Kongtong Sect, along with every martial faction in the area, had been keeping watch for some time. We were able to gather our forces quickly.”

“Which means…”

“Thirty thousand. That’s how many we’ve assembled so far. We’ve mobilized every resource Gansu Murim has.”

“……!”

“……!”

The leaders’ eyes widened. Mine were no different.

*Thirty thousand?*

That was an enormous army.

It was all the more astonishing when I remembered that Shanxi Province had fielded only fifteen thousand to hold Eight Spring Gorge and face the Great Steppe’s forces.

What was more, Sima Gong had specified *Gansu Murim*. That meant all thirty thousand were martial artists.

There was no comparing that to Shanxi Province, where more than half the total force had been government soldiers.

Of course, Shanxi Murim had already suffered severe losses in its conflict with the Mount Heng Sword Sect and the Head Elder’s betrayal. Even taking all of that into account, a force of thirty thousand was still almost unimaginable.

“W-where did you find that many people?”

Just as the Wind-and-Cloud Sword Lord spoke up to ask the question that must have been on everyone’s mind, Jeok Cheongang, who’d been watching with a frown, suddenly spoke.

“Unorthodox types are nothing without numbers. Isn’t that right?”

Sima Gong gave a small smile and nodded.

“I can’t deny it.”

“But still, a force of thirty thousand would be nearly impossible even for the Nine Sects and One Gang of the Central Plains.”

“That’s also true. Would the Great Nation have stood idly by if this many ruffians, liable to turn the swords at their waists against the state at any moment, had gathered?”

The phrase “the government and Murim shall not interfere in one another’s affairs” had been rendered practically meaningless ever since the Son of Heaven declared Dark Heaven a traitor. But there was a reason the principle had come into being in the first place.

It was an unspoken rule that had arisen naturally alongside Murim itself.

A stone that stuck out was bound to get hammered down sooner or later.

The countless martial factions scattered across the vast world had repeatedly checked one another and made agreements to avoid conflict. And so long as the foundations of the nation weren’t threatened, the Great Nation turned a blind eye to their existence.

People even said that when a dynasty fell, Murim remained.

But the Murim of Gansu had now crossed that unspoken line.

They’d gathered thirty thousand martial artists in the frontier, not even the Central Plains. That was an army they couldn’t have raised even if they’d turned every martial faction in Gansu Province upside down and shaken them out.

*Which means…*

There was only one possibility left.

The majority had no affiliation with any particular sect. They were the sort of people who followed only their own needs and interests.

“You even scraped together the dark-path figures. You must’ve been pretty desperate.”

The dark path.

At the mention of those who’d existed in an uneasy coexistence with Murim for ages beyond counting, several people’s expressions darkened. The Wind-and-Cloud Sword Lord’s eyes in particular sank.

“Sect Leader Sima. Is what Great Hero Jeok said true?”

Sima Gong answered calmly.

“It’s true that some of them are dark-path figures. Is that a problem?”

“……Well…”

“I’ll admit it. I’m an unorthodox martial artist, and the Yangtze River Channel League and the Green Forest Alliance are dark-path organizations to the core. Ah, and my son over there is the same.”

At his father’s sudden callout, Sama Pyo’s eyes, which had been silent all this time, wavered.

But the moment Sima Gong spoke again, the people had no choice but to turn their attention back to him.

“And everyone I just mentioned has one thing in common. Do you know what it is?”

They did. Everyone in the room did.

But the people remained silent, their faces heavy.

Everyone but one man.

“They’ve fought for the Murim Alliance—and they’re fighting for it now.”

Jeok Cheongang.

Sima Gong’s reflection appeared in his reddish, fever-bright eyes, befitting the title of Fire King.

“Unorthodox, dark-path figures, or nobodies who crawled in from God knows where—I don’t give a damn. If the weapons in their hands are pointed at Dark Heaven, that’s all that matters.”

Sima Gong nodded, his expression firm.

“As it was in the past, so it will be this time.”

“I’m not doubting you. But the kind of dark-path trash that would drift all the way out to this frontier must be rotten to the core. If something goes wrong…”

“I’ll stake my head on it.”

Then Jeok Cheongang, who’d been staring silently at Sima Gong, suddenly turned his head and swept his gaze across the room.

“What do you all think?”

There were respected elders of Gansu Murim gathered here who’d come out to greet us with Sima Gong, but Jeok Cheongang wasn’t asking them.

He was asking the senior members of the Zhongnan Sect who’d come with us.

As the Wind-and-Cloud Sword Lord, standing at their center, hesitated to answer, his Senior Brothers, the Roaring Fury Swordsman and the Taeeul Merciless Sword, spoke one after the other.

“Someone once said that it doesn’t matter whether a cat is white or black, as long as it catches mice.”

“The Sima Gong I know is a comrade-in-arms and a hero, someone who weathered the war alongside us, before he is an unorthodox martial artist. That a man like him should have to stake his life on this—isn’t that a crying shame?”

As I watched the two old Daoists pour out their words with practiced fluency, as if they’d been waiting for this, Jeok Cheongang’s gaze suddenly shifted to me.

“So, are you done stuffing your face with honey?”

At his question about why I was sitting there with my mouth full, pretending to be mute, I licked my lips and answered.

“Yeah. It was sweet.”

“You’ve been holding that precious honey in your mouth long enough. Now you must have something to say.”

“Is this something I get to decide?”

“Not a chance. Who do you think you are?”

I let out a snort, then slowly looked around.

Most of the faces were unfamiliar. I didn’t know their names or their epithets.

There were senior members of the Black Dragon Demon Gate and leaders of Gansu Murim, each of them heading a martial faction large or small.

At the center of them all stood Sima Gong.

“Can I ask a few questions?”

“Anything.”

“I can’t imagine you decided all of this on your own. Am I right?”

“Of course. The Sect Leaders gathered here and the Kongtong Sect agreed as well.”

“Then what if Dark Heaven isn’t targeting Gansu…”

“We’ll leave some forces behind and head straight for Qinghai. But that won’t happen.”

“Why not?”

“The signs are ominous. The Demonic Cult may have become Dark Heaven, but the enemies beyond the desert have always been our greatest concern. That remained true even after the Great Faction War.”

“What signs?”

“It’s too early to say. I’ve already selected people I can trust and sent them to scout beyond the desert. We’ll know for certain when they return. So…”

Sima Gong’s gaze moved from me to Jeok Cheongang.

“Please leave Gansu’s defenses to us and go to Qinghai, Senior. Even with reinforcements from Huashan and the others, Qinghai seems to be the place where every moment counts most.”

“Qinghai, Qinghai…”

Jeok Cheongang murmured the name in a low voice, almost like a groan.

That was when it happened.

“L-Lord Sect Leader!”

A frantic voice rang out from between the tightly shut doors.
```

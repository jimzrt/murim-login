<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1146.txt",
      "sha256": "710f577652f5457de01f61ae869c05c9a26e335ede9a0953897f89bd439c949c",
      "bytes": 12446
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ebce5372760dbb9fd743c2808871d01afc64ffc24043ced2facf96b02c893535",
      "bytes": 1122
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "590e227f6652008e661a5c9624697025c1d16f377a5ff81370b8d975e672de8e",
      "bytes": 246053
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "52ff3e9d01832525f50fbcd395ab33d5280b490e1c605a72b5e51d28f1dbbc2b",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c70aa752e00fe43f98f8f5bccb2b64249d01ad98896ed4abc1e4f414c2ba3a74",
      "bytes": 1672
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3f74e0985bf273a8d0de3997a90c31ee5c2a5f56a2476d8a4be9afa7d161b705",
      "bytes": 623
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "1e634bb24e25620396f9aa3a76addceff9196627cc771d2ddc7590453707571f",
      "bytes": 635
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "cce626cca86fce2336c319df33393c72edd421d49bb4fd55171f138abab174f0",
      "bytes": 291430
    }
  ],
  "estimated_tokens": 8760
}
-->

# Durable State Update — Chapter 1146

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
1 and safe_through 1146. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1146. Profile updates may replace only one
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
  "chapter": 1146,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1146,
    "continuity_sources": [1146],
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
    "Taekyung’s consciousness is in the realm of immortals while his body sleeps in Murim; he promised Jeok Cheongang he would return.",
    "Jeok Cheongang remains beside Taekyung and intends to protect him on the march to Tianshan.",
    "The coalition army of more than two hundred thousand is crossing the Taklamakan Desert toward Tianshan.",
    "The Grand Mage has been reborn through the Lord of Heaven’s grace and felt a wave; the Lord says the heavens have opened again, as green light rises over jade."
  ],
  "continuity_sources": [
    1145
  ],
  "open_questions": [
    "What caused the wave that the Grand Mage felt and the Lord of Heaven acknowledged?",
    "What does the Lord of Heaven mean when he says the heavens have opened again?",
    "What danger awaits the coalition army at Tianshan?"
  ],
  "safe_through": 1145,
  "temporary_decisions": [
    "Render 仙界 as “realm of immortals.”",
    "Render 塔克拉玛干 as “Taklamakan Desert.”",
    "Render 汗血寶馬 as “sweat-blood horse.”",
    "Render 時辰 as “shichen.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1145
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1145
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, and the Son of Heaven has formally enfeoffed him as Prince Shangshan.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1145
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 819
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and resolute under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

## Korean source

```text
＃1146화



어둡고 좁은 방 안, 커다란 전신 거울 앞에 선 남자는 매끄러운 표면을 말없이 응시하고 있었다.

호리호리한 장신의 체격과 뚜렷한 이목구비.

지난 삼십여 년간 수도 없이 보았던 자신의 모습이었으나, 지금 이 순간 그를 사로잡고 있는 감정은 익숙함이 아닌 씁쓸함과 분노였다.

“왜 하필 너일까.”

불현듯 입술 사이로 흘러나온 희미한 음성.

평소의 그였다면 결코 혼잣말 따위를 중얼거리지 않았겠지만, 남자는 개의치 않고 말을 이어갔다.

“이곳에 있어야 할 사람은 네가 아니야.”

한 마디, 한 마디마다 불길을 토해 내는 기분이다.

보이지 않는 예리한 송곳이 들쑤시는 것처럼 폐부 깊숙한 곳이 아리고, 어느샌가 흥건히 맺힌 땀방울은 뺨을 타고 밑으로 굴러떨어졌다.

그의 마음처럼. 끝없이.

“넌 자격이 없어.”

맞다.

충분한 ‘자격’을 갖춘 몇몇 극소수의 인물과는 달리 남자에게는 압도적인 무력도, 백전노장의 경험도 없었다.

그러나 그 사실을 인정하는 것과는 별개로 그는 누구보다 잘 알고 있었다.

자신의 어깨를 짓누르는 이 막중한 책임감의 무게와 이번 임무의 중요성을.

파르르 떨리던 눈동자가 일순간 번뜩인 것은 바로 그때였다.

으득.

섬뜩한 파육음과 함께 입안 가득 퍼져 나가는 혈향.

한 줌의 핏물을 뱉어 낸 남자는 다시금 거울과 마주했다.

조금 전과 달리 깊고 흔들림 없는 눈빛을 지닌 한 사내가 바로 그곳에 있었다.

그와 가장 길고 끈끈한 인연으로 연결되어 있는 동시에, 한편으로는 세상 그 누구보다 멀게 느껴졌던 누군가를 쏙 빼닮은.

하지만 이 짧은 감상조차 남자, 아니 최민우에게는 사치였다.

쩌적.

일순간 천장으로부터 전해지는 미세한 진동과 함께 전신 거울 위로 거미줄처럼 번진 실금.

마침내 때가 왔음을 직감한 최민우는 거울 속 일그러진 자신의 얼굴을 뒤로한 채 돌아섰다.

그리고 잠시나마 냉혹한 현실을 가로막아 주었던 녹슨 철문을 힘주어 열어젖혔다.

끼이익.

성인 남성 두 사람이 간신히 어깨를 나란히 할 수 있을 만큼 좁은 복도의 한 가운데, 군용 판초 우의로 전신을 가린 거한이 최민우를 향해 고개를 까딱였다.

“딱 맞춰 나왔군.”

“기다리게 해서 미안합니다. 잠시 준비가 필요해서.”

“미안해할 필요는 없다. 이곳의 지휘관은 너니까. 물론…….”

푸스슥.

조금 전보다 미세하게 커진 진동과 함께, 천장에서 천천히 떨어지는 먼지를 힐끗 바라본 그가 덧붙였다.

“더 늦었으면 곤란해졌겠지. 우선 가자고.”

약속이라도 한 것처럼 빠른 속도로 발걸음을 옮기기 시작한 그들은, 개미굴처럼 구불구불하게 이어진 복도를 지나치며 대화를 주고받았다.

“무슨 일입니까?”

최민우의 물음에 거한이 착 가라앉은 음성으로 대답했다.

“단순한 모래 폭풍이면 좋겠지만…….”

“놈들이군요.”

“빌어먹을, 그래.”

어째서 불길한 예상은 항상 빗나가는 법이 없을까.

그러나 모든 자책과 불평은 이미 깨진 거울 앞에서 내려놓고 왔다. 최민우는 흔들리려는 마음을 굳게 다잡으며 재차 입을 열었다.

“규모는 어떻게 됩니까?”

“지금까지 파악한 바로는 최소 수천 단위.”

수천.

얼핏 들으면 무책임하리만치 광범위한 수치였지만, 통신을 비롯하여 모든 레이더망은 진작 마비된 상황.

그렇기에 최민우는 어떤 고민이나 의심도 없이 거한의 말을 사실로 받아들였다.

거한의 힘은 이 낡고 오래된 지하 방공호(Bomb Shelter)에 머무르고 있는 그 누구보다 특별할뿐더러, 최민우 자신의 목숨도 맡길 만큼 신뢰할 수 있는 존재였으니까.

“……수천, 입니까.”

지금껏 파악한 바로만 수천이라면, 상황에 따라 만 단위를 넘어설 수도 있다는 뜻.

한층 무거워진 최민우의 눈빛에 거한이 애써 고개를 저었다.

“단순한 수색대일 수도 있다. 평소에도 워낙 개미 떼처럼 몰려다니는 놈들이니까.”

일리가 있는 추측이었다.

이미 광활한 사막 일대를 집어삼킨 적들의 숫자는 끔찍하리만치 많았고, 그것으로도 모자라 나날이 증가하고 있었으니.

‘만약 수색이 아닌 공격이 목적이 아니라고 해도, 다른 도시로 향하는 와중에 단순히 이동 경로가 겹쳤을 가능성도 충분해.’

최민우는 말없이 걸음을 옮기며 생각에 잠겼다.

지금 그들이 머무르고 있는 곳은 걸프전 당시 미군이 비밀리에 세운 지하 방공호.

종전 이후 이미 오십 년도 넘게 방치된 데다, 도중에 있었던 대격변으로 인해 지형이 뒤바뀌며 그 존재조차 잊힌 장소다.

어느 날, 다급히 사막을 가로지르던 일단의 무리가 모래 언덕 아래에 숨겨진 입구를 발견하기 전까지는.

‘그럼 우리도 운 좋게 발견한 이곳을 적들이 알고 있을 가능성은?’

두말할 것도 없이 희박하다.

다만 한 가지 마음에 걸리는 것이 있다면 얼마 전 가까스로 닿았던 통신 마법뿐인데, 발신자의 신분을 생각한다면 그마저도 적들이 알아차릴 가능성은 제로에 수렴했다.

‘그렇다는 건 결국.’

최민우는 마침내 한 가지 결론에 도달했다.

이 모든 것은 단순한 우연이라는 결론에.

앞서 거한의 말처럼 수색대이거나, 단순히 이동 경로가 겹쳤을 뿐일 가능성이 매우 높은 상황.

그러니 그들은 단지 기다리기만 하면 된다.

이 낡고 퀴퀴한 공간 속에서 숨죽인 채, 머리 위로 쏟아지는 모래 먼지를 맞으며 혹시 모를 전투를 대비하고 있으면 얼마 지나지 않아 평화가 찾아올 것이다.

저 초대받지 않은 불청객들은 숨겨진 집의 초인종도 찾지 못한 채 금세 그들의 머리 위를 지나갈 테고, 최민우는 남은 이들을 이끌고 아무런 피해 없이 이 방공호를 떠날 수 있다.

앞으로 고작 몇 시간 뒤에는.

그래.

그것만이 최선이다.

‘……그런데 왜.’

일순간, 발걸음을 멈춘 최민우의 모습을 본 거한이 눈을 크게 떴다.

“왜 그래? 혹시 무슨 문제라도 있나?”

잠시 침묵하던 최민우가 대답했다.

“아뇨. 아닙니다.”

“젠장, 깜짝 놀랐네. 거의 다 왔으니까 합류하자고. 다들 불안에 떠는 아기새마냥 짹짹거리고 있을 테니까.”

고개를 절레절레 내저은 거한이 중앙으로 통하는 마지막 복도를 향해 다시 걸음을 뗀 그때였다.

군용 판초 우의에 뒤덮인, 곱사등이 마냥 불룩 솟아 있는 거한의 등이 최민우의 눈에 들어온 것은.

그리고 동시에, 굳게 닫혀 있던 그의 입술이 열렸다.

“당신은, 최선이 뭐라고 생각합니까?”

“뭐?”

생각지도 못한 질문을 들은 거한이 고개를 돌렸다.

코에 닿을 만큼 깊게 눌러쓴 우의 아래, 황금을 녹여 만든 듯한 머리카락이 흘러내렸다.

“너, 갑자기 그게 무슨…….”

“판단이 되질 않습니다. 무엇이 옳고 그른지. 최선과 최악이 무슨 차이인지.”

최민우는 갈라진 음성으로 말을 이었다. 어느샌가 잘게 떨리고 있는 그의 눈동자는, 거울 안에서 보았던 그것과 같았다.

“지금 이 순간에도 열 배가 넘는 적들이 이곳으로 오고 있습니다. 하지만 잠자코 기다리면 불필요한 희생은 없을 겁니다. 놈들은 이곳을 모를 테니까.”

구구궁.

더욱 커진 진동이 천장을 뒤흔든다. 두 사람이 지나쳐 온 복도의 거리만큼, 울림 역시 강해져 있었다.

“앞으로 십 분만 대기한다면, 모든 게 끝나 있을 겁니다. 적어도 우리는.”

힘없이 툭 덧붙여진 뒷말에, 거한의 눈동자가 깊어졌다.

“하고 싶은 말을 해 봐.”

“적들의 목적이 무엇이건, 이 근방 어디에선가는 반드시 피가 흐를 겁니다. 제아무리 놈들의 머릿수가 많아도 수천이나 되는 병력을 아무런 이유 없이 움직이진 않을 테니까요.”

“듣고 보니 맞는 말이군. 그래서?”

“이 복도를 지나고 나면, 저는 지휘관으로서 명령할 겁니다. 살아서 고향으로 돌아가고 싶거든 숨도 쉬지 말고 대기하라고. 적들이 쫓고 있는 게 힘없는 민간인이든 헌터든, 절대 상관 말라고.”

둑이 허물어지듯 단숨에 말을 쏟아낸 최민우는 크게 심호흡 했다.

그리고 거의 수명이 다한 전구로부터 흘러나오는 희미한 불빛 아래에 드러난, 거한의 입매를 보았다.

“그래, 무슨 말을 하는지 알겠다. 그러니까…….”

그는 웃고 있었다.

“헛소리 다 했으면, 이제 진짜 하고 싶은 말을 해 봐.”

“……!”

“어디 한번 속 시원하게 말해 보라고. 우리가 잘 아는 그놈처럼.”

이제는 걷잡을 수 없을 만큼 커진 울림 속, 거한은 흔들리는 바닥에 털썩 주저앉았다.

마치 최민우의 대답이 있기 전까지는, 한 걸음도 움직이지 않겠다는 듯이.

“왜, 그놈처럼은 못 하겠나?”

최민우는 대답 대신 떨리는 주먹을 말아쥐었다.

거한이 말하는 ‘그놈’이 누구인지는, 이름을 듣지 않아도 잘 알고 있었다.

이미 오래전부터 가까운 곳에서 그를, 진태경을 지켜보았으니까.

그가 어떤 위기 속에서도, 늘 자신의 행동에 책임을 졌다는 것 역시도.

그리고 그건, 최민우로서는 도저히 메울 수 없는 차이였다.

“진태경 헌터는…… 나와는 다릅니다.”

“뭐가 다르지?”

“나는 약합니다. 그와는 비교도 할 수 없을 정도로. 동시에 이곳의 지휘관으로서 반드시 성공시켜야 할 임무가 있습니다.”

“책임감이라, 중요하지. 하지만 그건 상관없어.”

의미 모를 그 한 마디에 최민우가 뭐라 대답하기도 전, 거한이 나직이 덧붙였다.

“이미 당장이라도 뛰쳐나가서 전투할 생각이거든. 남아 있는 놈들 전부.”

“……!”

“아까 오는 길에 들러서 놈들의 머릿수를 말해주니 장비부터 챙기더군. 저렇게 개떼처럼 몰려가는 데에는 그만한 이유가 있을 거라고. 더 웃긴 건 뭔지 알아?”

거한이 피식 웃었다.

“지휘관 명령 기다리랬더니, 어차피 네 생각도 똑같을 거라고 하더라고.”

거한은 자리에서 일어나 석상처럼 굳어 있는 최민우를 향해 다가갔다.

아니, 움직인 것은 그 한 사람뿐만이 아니었다.

“저기, 그.”

“저희 언제 출동합니까?”

어느샌가 복도 끝자락에서 고개만 쑥 내민 헌터들의 모습에, 어깨를 으쓱한 거한이 최민우를 바라보았다.

“그렇다는군.”

최민우는 말없이 거한과 모든 준비를 끝낸 헌터들을 번갈아 바라보았다. 

그리고 천천히.

아주 천천히, 이제는 천둥처럼 사방을 뒤흔드는 거대한 울림 속에서 허리춤에 걸쳐진 검을 뽑았다.

“이게 제 대답입니다.”

그 순간.

츠츠츠츠, 서걱!

검신을 타고 맹렬하게 솟구친 오러(Auror)가, 방공호의 콘크리트 벽을 두부처럼 갈랐다.

콰아아앙!

폭발과 동시에 비산하는 파편.

그 너머로 스며드는 뜨거운 햇빛과, 저주받은 괴물들의 핏물.

“역시, 인간치고는 마음에 들어.”

거한, 스켈레톤 킹이 소리 내어 웃으며 판초 우의 아래 숨겨 놓은 대형 배낭을 툭툭 두드렸다.

“너는 이 몸이 잘 지켜 줄 테니 걱정마라. 쓸데없이 잠만 많은 인간.”

그리고 적들을 향해 쏘아졌다.

아니, 그러려고 했다.

누구도 생각지 못한 대답이 들려오기 전까지는.

“아빠 안 잔다.”

“……어?”
```

## Final English reading copy

```markdown
# Chapter 1146

In a dark, narrow room, a man stood before a full-length mirror, silently staring at its smooth surface.

Tall and slender, with sharply defined features.

He had seen his own reflection countless times over the past thirty-odd years. But the feelings gripping him now weren’t familiarity, but bitterness and anger.

“Why did it have to be you?”

The faint words slipped suddenly from his lips.

Normally, he would never have muttered to himself. But the man didn’t care, and continued.

“You’re not the one who should be here.”

Each word felt like it was spitting fire.

A sharp, invisible awl seemed to probe deep inside his chest. Sweat had gathered on his face, then rolled down his cheek.

Like his heart. Endlessly.

“You don’t deserve it.”

That was right.

Unlike the handful of people who possessed the necessary “qualifications,” the man had neither overwhelming power nor the experience of a battle-hardened veteran.

But even apart from whether he could accept that truth, he knew better than anyone the weight of the immense responsibility pressing down on his shoulders—and how important this mission was.

That was when his trembling eyes suddenly flashed.

Crack.

With a gruesome sound of flesh tearing, the taste of blood spread through his mouth.

The man spat out a mouthful of blood, then faced the mirror again.

There stood a man with a deep, unwavering gaze, unlike the one from moments ago.

He bore an uncanny resemblance to someone bound to him by the longest and closest of ties—and yet, someone who had never felt farther away.

But even this brief reflection was a luxury for the man—no, for Choi Minwoo.

Crack.

A faint tremor traveled down from the ceiling, and hairline fractures spread across the full-length mirror like a spiderweb.

Sensing that the time had finally come, Choi Minwoo turned away, leaving behind his distorted reflection, and flung open the rusted iron door that had briefly shielded him from the harsh reality outside.

Creeeak.

In the middle of a corridor barely wide enough for two adult men to stand shoulder to shoulder, a hulking figure wrapped from head to toe in a military poncho raincoat gave Choi Minwoo a nod.

“Right on time.”

“Sorry to keep you waiting. I needed a moment to get ready.”

“No need to apologize. You’re in charge here. Though…”

The figure glanced at the dust drifting slowly down from the ceiling, stirred by a tremor that had grown slightly stronger.

“Any later and we’d have been in trouble. Let’s move.”

As if they’d planned it, they quickly set off, trading words as they made their way through the winding, ant-nest-like corridors.

“What happened?”

At Choi Minwoo’s question, the hulking figure answered in a low voice.

“Hopefully it’s just a sandstorm…”

“It’s them.”

“Damn it. Yeah.”

Why were ominous hunches never wrong?

But he’d left all his self-reproach and complaints behind him in front of the broken mirror. Choi Minwoo steeled himself and spoke again.

“How many?”

“From what we’ve figured out so far, at least several thousand.”

Several thousand.

At first glance, it was a recklessly broad estimate. But communications and every radar network had been down for some time.

So Choi Minwoo accepted the figure without question or hesitation.

The hulking figure’s abilities were unlike anyone else’s in this old, worn-out underground bomb shelter. He was also someone Choi Minwoo trusted enough to entrust with his own life.

“…Several thousand?”

If there were already several thousand as far as they could tell, the number could exceed ten thousand, depending on the situation.

At Choi Minwoo’s darkening gaze, the hulking figure made an effort to shake his head.

“They might just be a scouting party. Those guys always move around in swarms like ants.”

It was a reasonable guess.

The enemy had already swallowed up a vast stretch of desert, their numbers horrifyingly large—and they were growing by the day.

*Even if they aren’t here to attack, they could simply be passing through on their way to another city. Our routes might have crossed by chance.*

Choi Minwoo walked in silence, lost in thought.

The place they were staying was an underground bomb shelter secretly built by the US military during the Gulf War.

It had been abandoned for over fifty years since the war ended. Then the Great Cataclysm reshaped the landscape, and the shelter was forgotten altogether.

Until one day, a group of people rushing across the desert discovered its entrance, hidden beneath a sand dune.

*And what are the odds the enemy knows about this place too, when we only found it by luck?*

Virtually none.

The only thing that bothered him was the communication Magic they’d barely managed to establish not long ago. But given who had sent it, the chance the enemy had picked up on it was close to zero.

*Which means, in the end…*

Choi Minwoo finally arrived at a conclusion.

That all of this was just a coincidence.

It was highly likely they were a scouting party, as the hulking figure had said, or that their routes had simply crossed.

So all they had to do was wait.

If they held their breath in this old, musty place, took the sand and dust raining down on them from overhead, and prepared for a possible fight, peace would return before long.

The uninvited guests wouldn’t even find the doorbell to their hidden home. They’d pass right over their heads, and Choi Minwoo could lead the survivors out of the shelter without a single casualty.

In just a few hours.

Yeah.

That was the best option.

*…Then why?*

The hulking figure’s eyes widened when Choi Minwoo suddenly stopped walking.

“What’s wrong? Something happen?”

After a brief silence, Choi Minwoo answered.

“No. Nothing.”

“Damn, you scared me. We’re almost there, so let’s join the others. They’ll be chirping away like nervous little chicks.”

The hulking figure shook his head and started down the last corridor leading to the central chamber.

That was when Choi Minwoo noticed his back, bulging beneath the military poncho like a hunchback.

And at the same moment, his tightly shut lips parted.

“What do you think the best choice is?”

“What?”

The hulking figure turned at the unexpected question.

Beneath his raincoat hood, pulled so low it nearly touched his nose, golden hair spilled out as if made of molten gold.

“What’s gotten into you all of a sudden…?”

“I can’t tell what’s right or wrong. What’s the difference between the best choice and the worst?”

Choi Minwoo continued in a hoarse voice. His eyes had begun to tremble, just like the ones he’d seen in the mirror.

“Even now, an enemy ten times our size is heading this way. But if we wait quietly, there won’t be any unnecessary casualties. They don’t know about this place.”

Rumble.

The growing tremors shook the ceiling. The rumbling had grown stronger with every step they’d taken down the corridor.

“If we wait just ten more minutes, it’ll all be over. At least for us.”

The last words fell from his lips, weak and abrupt. The hulking figure’s eyes grew more serious.

“Say what you want to say.”

“Whatever the enemy’s goal, blood is sure to be spilled somewhere nearby. No matter how many of them there are, they wouldn’t move thousands of troops without a reason.”

“Now that you mention it, you’re right. So?”

“Once we’re through this corridor, I’ll give the order as their commander. If you want to make it home alive, hold your breath and wait. Don’t get involved, whether the enemy’s chasing helpless civilians or Hunters.”

Choi Minwoo let it all out at once, like a dam giving way, then took a deep breath.

In the faint light from a bulb nearing the end of its life, he saw the hulking figure’s mouth.

“Yeah, I get what you’re saying. So…”

He was smiling.

“If you’re done with the bullshit, tell me what you really want to say.”

“...!”

“Come on, say it and get it off your chest. Like that guy we know so well.”

Amid the now-uncontrollable rumbling, the hulking figure dropped onto the shaking floor.

As if he wouldn’t take another step until Choi Minwoo answered.

“What, can’t do it like him?”

Instead of answering, Choi Minwoo clenched his trembling fist.

He knew who the hulking figure meant by “that guy,” even without hearing his name.

He’d been watching him from close by for a long time now—Jin Taekyung.

And he knew that no matter what crisis he faced, Jin Taekyung always took responsibility for his actions.

That was a gap Choi Minwoo simply couldn’t close.

“Hunter Jin Taekyung… is different from me.”

“How?”

“I’m weak. I can’t compare to him. And I have a mission I absolutely have to succeed at, as the commander here.”

“Responsibility matters. But that has nothing to do with it.”

Before Choi Minwoo could respond to the cryptic remark, the hulking figure added quietly:

“The others still here are already planning to rush out and fight. Every last one of them.”

“...!”

“I stopped by on the way and told them how many enemies there were. First thing they did was grab their gear. They figure there must be a reason for that many of the bastards to be swarming around. Want to hear the funniest part?”

The hulking figure gave a short laugh.

“I told them to wait for the commander’s orders. They said they figured you’d think the same way anyway.”

He rose and approached Choi Minwoo, who stood frozen like a statue.

And he wasn’t the only one who moved.

“Uh, hey…”

“When are we heading out?”

At some point, Hunters had poked their heads out from the far end of the corridor. The hulking figure shrugged and looked at Choi Minwoo.

“Sounds like they’re ready.”

Choi Minwoo silently looked from the hulking figure to the Hunters, already fully prepared.

Then, slowly.

Very slowly, amid the enormous rumbling that now shook the surroundings like thunder, he drew the sword at his waist.

“This is my answer.”

At that moment—

Shhhhhk! Slash!

The aura surging fiercely along the blade split the shelter’s concrete wall like tofu.

KABOOM!

Debris flew everywhere in the explosion.

Beyond it came the blazing sunlight—and the blood of cursed monsters.

“Not bad for a human.”

The hulking figure, the Skeleton King, laughed aloud and patted the large backpack hidden beneath his poncho.

“Don’t worry. I’ll protect you. You uselessly sleepy human.”

And he shot toward the enemies.

Or he would have.

If not for the answer no one had expected.

“Dad’s not sleeping.”

“…Huh?”
```

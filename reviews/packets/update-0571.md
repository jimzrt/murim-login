<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0571.txt",
      "sha256": "3a93d5b3bbf85636f471610299c8131b187a564c1b9e35d815a3d7e04695e1dd",
      "bytes": 13051
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3badeac0f772e47629ae11913b54d1d6a69bc976ac0bb99e5481ce4f69d0093b",
      "bytes": 5088
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6542fa82e18d41880799ac707cc8b09c7ddf0dff88f0a7d87baff6f7f7cae7f7",
      "bytes": 180556
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8b517e10b03923a0e3d247691cca1e2330c0312285700a75fe198c5178cfa1c0",
      "bytes": 176182
    }
  ],
  "estimated_tokens": 9177
}
-->

# Durable State Update — Chapter 571

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 571. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 571. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 571,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 571,
    "continuity_sources": [571],
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
    "The worldwide Gate and monster crisis may mark the beginning of a second Great Cataclysm; rising magic power readings are strengthening monsters, Mutated Gates now appear roughly every three days, and Hunter shortages are worsening.",
    "The Pocheon Mutated Gate three days earlier was stopped before a Monster Wave by Peace Guild's Emergency Rescue Team, with no deaths or civilian casualties.",
    "Team Leader Choi says the crisis has exceeded the limit of national concealment and is prioritizing Gate defenses despite reducing Peace Guild's raid capacity; she is working with Song Cheonwoo against Go Jun's control of Ares Guild while Song knows where Cheon Taemin is hidden.",
    "Taekyung is a Supreme Peak master publicly recognized as S-rank-level while retaining an A-rank license, leads the Fire Dragon Pavilion's first Nanman mission, and is Peace Guild's wealthy modern-world patron.",
    "The six-member Fire Dragon Pavilion mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is Can't Go to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong.",
    "Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants, while the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains.",
    "Go Jun has become increasingly ruthless, controls Ares Guild's legacy, has seized Song Cheonwoo's children as leverage, and appears to be arranging Song's quiet elimination; Go Se-won commands Ares Guild's thirty-member A-rank security team while remaining obedient despite growing moral conflict.",
    "The Skeleton King was the person who applauded Taekyung and appeared as King Fury; Taekyung trusts him enough to handle suitable emergencies alone and has granted him greater freedom.",
    "Taekyung has spent up to three days isolated in training, nearly completing an as-yet-unidentified new martial endeavor, while abnormal Gates and emergency rescue demands increase.",
    "Lee Dongseok is using a changed face and assumed name to enter the Haeundae C-rank Gate Siren's Black River while carrying a valuable dangerous object and fulfilling an undisclosed life-threatening mission; he regards Lee Jungryong as a father."
  ],
  "continuity_sources": [
    570,
    569
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What caused the Haeundae Gate's transformation, what is the object entrusted to Lee Dongseok, and what does his mission require?",
    "What will result from the duel between Jeok Cheongang and Nangong Cheon, why did Ju Hwaran and Sama Pyo's political engagement end, whether Song Cheonwoo's children survive Go Jun's plan, and what will Taekyung's unfinished training project become?"
  ],
  "safe_through": 570,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, 고잉메리호 as Going Merry, 부산 as Busan, 해운대 as Haeundae, 포천 as Pocheon, 경기도 as Gyeonggi Province, and 세이렌의 검은 강 as Siren's Black River.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 투로 as combat sequence, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 현혹 마법 as enchantment magic, 장거리 텔레포트 마법진 as long-distance Teleportation magic, 킹 퓨리 as King Fury, 배리어의 국장 as Director of Barrier, 세종 기지 as King Sejong Station, 마력 수치 as magic power reading, 이동석 as Lee Dongseok, 동석 씨 as Dongseok, 팀장님 as Team Leader, and 전 부길드장님 as former Vice Guild Master."
  ],
  "version": 1
}
```

## Exact glossary matches

| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 시스템              | **System**                     |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 청해     | **Qinghai**            |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 광안 | **Guang'an** | Sichuan location where the party boards Mu Song's ship. |
| 탈진 | **Exhaustion** | System status effect caused by exhausting all internal energy while severely injured. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

(No chapter-safe profiles matched.)

## Korean source

```text
＃571화



부산.

대격변 이전에도, 이후에도 국내에서 세 손가락에 드는 인구수를 보유한 대도시다.

지금으로부터 아주 오래전, 부산으로 가족 여행을 온 어느 잘생기고 똑똑한 초등학생은 밤마다 창문에 들러붙어 있다시피 했더랬다.



‘태경아. 뭘 그렇게 보고 있어?’

‘다리! 반짝거려! 예뻐!’

‘워어, 진짜네. 피팅 모델인가?’

‘……그 다리 아니야. 아빠.’

‘아.’

‘쩌어기 저 다리! 길고 반짝거리는 거!’

‘아하. 광안대교?’

‘광안대교? 광안대교가 뭐야?’

‘저 다리 이름이야. 아까 태경이도 보긴 했을 텐데, 확실히 밤에 보니까 더 예쁘지?’

‘응응! 나 가 볼래! 지금 당장 광안대교 데려다줘!’



떼를 쓰는 어린 아들을, 아버지는 사랑스러워 죽겠다는 눈빛으로 바라보았다.



‘어이구, 우리 아들. 아빠 하루 종일 운전하느라 피곤해 죽겠는데 자기만 생각하는 것 봐. 누굴 닮아서 이럴까?’

‘그럼 엄마한테 피팅 모델이 뭐냐고 물어봐도 돼?’

‘……내 새끼 맞구나. 가방 챙기렴.’



인생에서 잊을 수 없는 순간 중 하나다. 침울해하는 아버지의 손을 잡고 찾아간 광안대교는 어린 초등학생의 내 뇌리에 선명한 흔적을 남겼다.

그것은 턱없이 크고 반짝였으며, 옆에는 늘 바쁜 탓에 많은 시간을 함께하지 못했던 아버지가 있었다.

목 디스크를 호소하는 아버지를 협박해 목말까지 타니 세상 부러울 것이 없었다.



‘아빠, 우리 다음 주에도, 다다음 주에도! 다음 달에도 또 오자! 그때도 목말 태워 줘!’

‘하하. 어쩌지? 태경이 말대로면 다음 달에는 못 올 것 같은데.’

‘왜?’

‘이대로면 다다음 주쯤에 아빠 목이 부러질 거거든. 태경이 요새 하루에 밥 몇 그릇 먹니?’

‘요새는 별로 입맛이 없어서 다섯 그릇!’

‘……장하다, 내 새끼. 어쩐지 밤하늘이 노랗게 보이더라.’



행복한 기억이다. 그날 우리는 함께 여러 가지 이야기를 나누었고, 잔뜩 신이 난 나는 호텔에 남아 있던 어린 하연이와 엄마에게 실컷 자랑했다.

그리고 그 모습을 보며 목을 주무르던 아버지는 피식 웃으며 약속했다.



‘하연이가 좀 더 크면, 태경이 네가 중학생이 되면 그때 다시 바다 보러 오자. 알았지?’

‘진짜?’

‘당연하지. 자, 약속.’



약속은 지켜지지 못했다.

두 자식이 커 가며 돈 들어갈 곳은 많았고 무리해서 부업을 하던 아내마저 병을 얻자, 아버지는 자연스럽게 바빠졌다.

평범했던 어느 날, 평범하지 않은 사고로 세상을 떠났다.

하지만 나는 그때의 약속을 기억하고 있었다.

비록 아버지는 더 이상 곁에 없지만, 어린 시절 보았던 광안대교의 모습은 이십여 년이 흐른 지금도 뇌리에 선명히 각인되어 있었다.

그리고 지금.

구구구궁.

내 눈앞에서, 광안대교가 무너져 내리고 있었다.

“아.”

나도 모르게 입술 사이로 흘러나온 탄식.

머리는 당장 죽을 힘을 다해 저곳으로 가라 하지만, 몸은 보이지 않는 손에 붙들린 것처럼 움직이지 않는다.

‘이미…… 늦었어.’

혼자만의 생각이 아니다.

함께 도착한 스켈레톤 킹도, 우리를 이곳까지 이동시킨 마법사도 탈진한 눈으로 수 킬로미터 밖에서 시작되고 있는 재앙을 지켜보고 있었다.

“아, 안 돼!”

이름도 모르는 마법사의 외침은 공허했고, 저 멀리 내려다보이는 광경은 압도적이었다.

‘저건…….’

파도다.

이제는 지켜질 수 없는 약속의 장소를, 하루에도 수천, 수만 대의 차량이 오가는 그곳을 덮친 것은 수십 미터에 달하는 거대한 파도였다.

콰아아아아!

엄청난 무게와 힘이 실린 파도는 높이 35m, 길이 7,420m에 이르는 광안대교의 허리 부분을 강타했다.

사방으로 튀는 물보라와 새하얀 포말 사이로 사람들의 비명이 파묻히고, 제한된 속도에 맞춰 느긋하게 이동 중이던 수백 대의 차량이 장난감처럼 튕겨 나갔다.

콰과과과광!

굉음과 함께 광안대교라 불리는 현수교(懸垂橋)의 주탑과 앵커가 박살 난다.

교량을 지탱하고 있던 수백 개의 케이블은 끊어짐과 동시에 거대한 채찍이 되어 사방을 후려쳤다.

쉬이이이이잉, 꽈앙!

그야말로 찰나의 순간이었다.

마치 개미처럼 보이는 사람들과 자동차가 케이블에 휩쓸려 사라졌다.

단말마도 남기지 못한 그들이 서 있던 자리에는 붉은 핏물이 흘렀고, 연쇄적인 폭발과 천운으로 살아남은 사람들의 비명.

그리고 미친 듯이 울리는 클락슨 소리가 곤두선 감각을 통해 전해졌다.

빵! 빠아아앙!

- 후진해! 빨리 후진하라고! 이 개새꺄!

- 꺄아아아아악!

- 아이! 아이 좀 꺼내 주세요! 여기 애가……!

마치 꿈이라도 꾸는 것처럼 몽롱하다.

마법과 과학으로 이루어진 첨단 문명이 모래성처럼 무너지고 있었다.

어린 시절의 추억이 서린 광안대교가 파괴와 죽음의 무게를 이기지 못하고 붕괴하고, 살아남은 이들은 차를 포기하고 미친 듯이 달리고 있었다.

누군가의 도움을 간절히 부르짖으며.

- 살려, 살려 주세요!

- 엄마아!

그리고 그들의 비명이, 석상처럼 굳어 있던 나를 깨웠다.

“아.”

구해야 한다. 이 재앙을 막아야 한다.

멈춰 있던 시간은 고작 수십여 초에 불과하나, 이미 수백이 죽었고 더 이상 망설인다면 수천, 수만이 죽을 것이다.

짝!

두 뺨을 힘껏 후려치자 강렬한 통증과 함께 정신이 돌아온다.

터져 나간 입 안에서 흐르는 피를 뱉은 나는 망설임 없이 스켈레톤 킹의 멱살을 잡아챘다.

덥석!

“어, 어?”

“간다. 정신 똑바로 차려.”

“자, 잠깐만. 어디 가는……!”

스켈레톤 킹의 물음이 끝까지 이어지기도 전에, 도움닫기를 끝마친 나는 온 힘을 다해 녀석을 창밖으로 내던졌다.

아니. 쏘아 보냈다.

콰창! 후우우우웅!

강화 마법이 걸린 통유리가 박살 남과 동시에 스켈레톤 킹의 신형이 포탄처럼 쏘아진다.

바람에 파묻히는 녀석의 비명을 들으며, 나도 힘껏 지면을 박찼다.

이미 탈진한 채 주저앉아 있는 마법사에게 한 마디를 남기는 것도 잊지 않았다.

“내 이름 대고 당장 구조 요청해요. 어디든, 당장!”

지칠 대로 지친 그가 제대로 들었을지, 구조 요청을 어디로 보낼지는 모르겠다.

지금 내게는 다른 어떤 것보다 눈앞의 상황이 중요했다.

콰앙!

온 힘을 쏟아부은 발돋움에, 텔레포트 마법진이 설치된 고층 빌딩이 부르르 떨린다.

까마득한 상공을 가르며 쏘아진 내게 누군가의 분노 어린 외침이 닿았다.

“이 미친 인간아!”

스켈레톤 킹이다. 자신만의 권능으로 뼈로 이루어진 날개를 만든 녀석은 빠른 속도로 날갯짓하며 다가왔다.

아니, 내가 막아서지 않았다면 그렇게 했을 것이다.

“다른 곳으로.”

“뭐?”

“범위가 넓어. 둘로 나눠서 커버한다.”

몬스터 웨이브(Monster Wave). 그것도 인구 밀도가 매우 높은 부산에서 벌어진 일이다.

매직 존슨을 통해 본 영상 속처럼 사막이나 인적이 드문 군사 구역이라면 모를까, 부산은 당장 반경 몇 킬로미터 안에 수천이 넘는 사람들이 바글바글한 곳이다.

무슨 수를 써서라도 불길이 번지는 것을 막아야 했다.

“내가 우선 다리를 맡는다. 너는…….”

“젠장, 알았다.”

시간이 없는 탓에 말이 짧았지만, 스켈레톤 킹이 알아듣기에는 충분했다.

마른침을 꿀꺽 삼킨 녀석의 시선이 까마득한 아래를 향했다.

비명과 혼란으로 잠식된 도로와 죽을힘을 다해 도망치는 사람을 훑던 시선이 문득 파르르 떨렸다.

“빌어먹을, 저건 또 뭐야.”

“뭐겠어.”

짤막하게 대답한 나는 인벤토리에 챙겨 둔 예비용 창 하나를 꺼내어 지상을 향해 겨누었다.

극대화된 안력(眼力)을 통해 보이는 그것의 모습은 여느 괴물들처럼 흉측했고, 전신을 뒤덮은 비늘과 턱까지 내려온 지느러미는 혐오스러웠다.

‘머맨(Merman).’

바다와 같은 환경에 서식하는 수중 몬스터.

남성체 인어(人魚)의 모습을 한 놈은 동화 속에서 묘사된 것처럼 아름답지도, 상냥하지도 않았다.

지금 이 순간 바다에서 솟구쳐 올라 사람들을 덮쳐 가는 수백 마리의 머맨 무리만 봐도 알 수 있는 사실이었다.

- 시시시시싯!

- 카룩!

알아들을 수 없는 기성을 토해 내며 내달리는 놈들의 손아귀에서 따개비가 달라붙은 삼지창이 번뜩인다.

그 끝에, 주저앉아 울고 있는 어린 여자아이가 있었다.

“으아아아앙! 엄마아!”

“민희야!”

아이의 울음. 뒤돌아본 부모의 비명.

그리고 첫 사냥감을 향해 달려드는 수백 마리의 몬스터.

‘지금.’

나는 몸을 중심을 이동시켰다.

비스듬히 기운 채 바람을 가르며 쏘아지던 신형이 급격히 아래로 향하고, 단전을 타고 흐른 공력이 발끝에서 발출된다.

파앙!

허공답보(虛空踏步)로 허공을 밟으며 시작된 급강하.

그러나 아무리 서두른다 하더라도, 이대로라면 내가 도착하기도 전에 아이가 목숨을 잃을 수밖에 없다.

‘가라.’

짧게 호흡한 나는, 지상을 향해 겨누고 있던 창을 흩뿌렸다.

쉬이이잉!

한 자루의 창이 까마득한 높이로부터 벼락이 되어 내리꽂힌다.

바람을 가르고, 공간을 지우고, 필살(必殺)이라는 두 글자를 담아…….

표적을 관통한다.

퍼걱! 콰드드드득!

선두에서 가장 먼저 아이를 향해 달려가던 머맨은 물론, 놈의 주위에 있던 십여 마리의 몬스터가 한 줌 핏물로 화했다.

동시에 움직임을 멈춘 수백 마리의 인어가 입을 벌린 채 하늘을 바라본다.

흉포함과 의문이 절반씩 뒤섞인 눈빛에, 내가 중얼거렸다.

“뭘 봐. 개새끼들아.”

인벤토리 오픈. 소환.

탁. 양손에 두 자루의 창이 잡힌 순간, 내 팔은 이미 지상을 향해 휘둘려지고 있었다.

퍼엉! 콰직!

강철보다 단단한 비늘이 부서지고 지느러미가 찢어진다.

운 좋게 절반의 몸뚱어리만 잃은 한 머맨이 구슬픈 단말마를 토해 냈다.

- 크룩, 크루루룩!

시끄럽다.

‘인벤토리 오픈. 소환.’

쉬잉! 퍼엉!

해가 중천에 뜬 정오 무렵. 때아닌 폭죽이 터진다.

기울어진 광안대교의 난간을 타고 끈적한 핏물이 주르륵 미끄러졌다.

‘더. 더. 한 번 더.’

오픈. 소환. 그리고 소환. 또 소환.

그야말로 찰나의 순간이었다. 시스템의 작동은 즉각적이었고, 내 움직임은 바람보다 빠르고 벼락보다 위력적이었다.

생각과 동시에 뻗어 나간 손은 불과 수 초 남짓한 짧은 시간 동안 수십 개의 창을 움켜쥐고, 지상을 향해 흩뿌려졌다.

‘죽어라.’

쉬이이잉, 퍼버버벙!

갈라진다. 터진다.

삼지창으로 막으려 했던 놈들은 삼지창과 함께, 황급히 도망치려던 놈들은 미처 발걸음을 떼지도 못한 채, 그렇게 죽어 갔다.

그로부터 불과 3m 떨어진 곳에서 주저앉아 울던 아이가 딸꾹질을 시작했을 때, 주위에 남은 것은 아무것도 없었다.

“끕. 흡.”

아홉 살쯤 되었을까. 작은 손으로 틀어막은 입에서는 울음 섞인 딸꾹질이 흘러나온다.

큼지막한 그 눈에는 지금 내 모습이 어떻게 비쳤을까.

괴물을 무찌른 괴물? 아니면 하늘에서 내려온 천사?

모르겠다. 하지만 한 가지는 확실하다.

‘넌…… 나와는 달리 이곳에 좋은 추억은 없겠구나.’

입맛이 씁쓸하다. 사뿐히 지면에 착지한 나는 아이를 달래는 대신 손가락을 까딱였다.

스르륵.

허공섭물. 부드럽게 뻗어 나간 기운이 아이를 밀어 낸다.

저 멀리, 울부짖으며 자식을 향해 뛰어오던 부모들을 향해.

하지만 저 가족의 불행은 아직 끝나지 않았다.

구구구구궁.

태양이 떠 있음에도 검게 물든 바다.

다시 한번 솟아오르는 수십 미터의 파도에 숨어 있는 ‘그것’을 응시하며, 나는 백염의 창날을 늘어트렸다.
```

## Final English reading copy

```markdown
# Chapter 571

Busan.

Both before and after the Great Cataclysm, it was one of the three most populous cities in the country.

A very long time ago, a handsome, clever elementary school student who had come to Busan on a family trip used to spend every night practically glued to the window.

*“Taekyung. What are you looking at so intently?”*

*“That leg! It’s sparkling! It’s pretty!”*[^1]

*“Whoa, you’re right. Is she a fit model?”*

*“……Not that kind of leg, Dad.”*

[^1]: The Korean word *dari* can mean either “leg” or “bridge.”

*“Oh.”*

*“That bridge over there! The long, sparkly one!”*

*“Aha. Gwangan Bridge?”*

*“Gwangan Bridge? What’s that?”*

*“That’s the name of the bridge. You must have noticed it earlier too, but it’s definitely prettier at night, right?”*

*“Yeah, yeah! I want to go there! Take me to Gwangan Bridge right now!”*

The father gazed at his demanding young son with an expression of such overflowing affection that he looked like he might die from it.

*“Oh, my son. Look at you, thinking only of yourself while your poor father is exhausted from driving all day. Who could you possibly take after?”*

*“Then can I ask Mom what a fitting model is?”*

*“……You really are my son. Pack your bag.”*

It was one of the unforgettable moments of my life. Visiting Gwangan Bridge hand in hand with my dejected father left a vivid mark on my young mind.

It was impossibly huge and glittering, and beside me stood my father, who had never been able to spend much time with me because he was always busy.

After threatening my father—who was complaining about a herniated disc in his neck—into carrying me on his shoulders, I felt like I had everything in the world.

*“Dad, let’s come again next week, and the week after that! And next month too! Carry me on your shoulders then too!”*

*“Haha. What should I do? If things go the way you want, I don’t think I’ll be able to come next month.”*

*“Why?”*

*“Because if this keeps up, my neck will be broken by the week after next. How many bowls of rice have you been eating a day lately, Taekyung?”*

*“I haven’t had much of an appetite lately, so only five bowls!”*

*“……That’s my good boy. No wonder the night sky looked yellow.”*

It was a happy memory. That day, they talked about all sorts of things together, and the excited young Taekyung proudly told Hayeon and his mother all about it when they returned to the hotel.

Watching him, his father rubbed his neck, gave a quiet laugh, and made a promise.

*“When Hayeon is a little older, and you’re in middle school, Taekyung, let’s come back to see the ocean. All right?”*

*“Really?”*

*“Of course. Here—promise.”*

The promise was never kept.

As his two children grew, there were more and more things to spend money on. When even his wife, who had pushed herself too hard with a side job, fell ill, his father naturally became busier.

On an ordinary day, he died in an extraordinary accident.

But I remembered that promise.

Even though my father was no longer by my side, the sight of Gwangan Bridge from my childhood remained vividly engraved in my mind even after more than twenty years.

And now—

*Ruuuumble.*

Gwangan Bridge was collapsing before my eyes.

“Ah.”

A sigh escaped between my lips before I could stop it.

My mind urged me to get there with every ounce of strength I had, but my body would not move, as though invisible hands had seized hold of it.

*It’s…… already too late.*

It was not a thought I had alone.

The Skeleton King, who had arrived with me, and the mage who had transported us here were also watching the disaster beginning several kilometers away with exhausted eyes.

“N-no!”

The cry of the mage whose name I did not know was hollow, and the scene spread out in the distance below us was overwhelming.

*That’s……*

A wave.

What had struck the place where a promise could no longer be kept—the place crossed by thousands, even tens of thousands, of vehicles every day—was a gigantic wave dozens of meters high.

*Whoooosh!*

Carrying tremendous weight and force, the wave slammed into the middle of Gwangan Bridge, a suspension bridge thirty-five meters high and 7,420 meters long.

The screams of people were swallowed by spray bursting in every direction and blinding white foam, while hundreds of cars traveling leisurely within the speed limit were tossed around like toys.

*Boom! Crash!*

With a deafening roar, the suspension bridge’s towers and anchors shattered.

The hundreds of cables supporting the bridge snapped and instantly became gigantic whips, lashing out in every direction.

*Whoooooosh—boom!*

It happened in the blink of an eye.

People and cars that looked like ants were swept away by the cables and vanished.

Red blood flowed where they had stood, unable even to leave a final scream behind. Chain explosions, the screams of those who had survived by sheer luck, and the frantic blaring of car horns all reached my heightened senses.

*Honk! Hooooonk!*

—Reverse! Reverse right now, you fucking bastard!

—Aaaaaaah!

—Please! Please get my child out! There’s a kid here……!

It felt hazy, as though I were dreaming.

An advanced civilization built on magic and science was crumbling like a sandcastle.

Gwangan Bridge, which held the memories of my childhood, could not withstand the weight of destruction and death and collapsed. Those who survived abandoned their cars and ran for their lives.

Desperately crying out for someone to help them.

—Save me! Please save me!

—Mommy!

And their screams woke me from where I had stood frozen like a statue.

“Ah.”

I had to save them. I had to stop this disaster.

Only a few dozen seconds had passed while I stood still, but hundreds had already died. If I hesitated any longer, thousands and tens of thousands would die.

*Smack!*

I slapped both cheeks as hard as I could. The sharp pain brought me back to my senses.

After spitting out the blood flowing from my split mouth, I grabbed the Skeleton King by the collar without hesitation.

*Grab!*

“W-wait?”

“I’m going. Get a grip.”

“W-wait a second. Where are you going……?”

Before the Skeleton King could finish his question, I completed my running start and threw him out the window with all my strength.

No.

I shot him out.

*Crash! Whoooosh!*

The reinforced floor-to-ceiling window shattered, and the Skeleton King’s body shot outward like a cannonball.

Hearing his scream disappear into the wind, I kicked off the ground with all my strength as well.

I did not forget to leave one instruction for the mage, who had already collapsed from exhaustion.

“Call for rescue using my name. Anywhere—right now!”

I had no idea whether the mage, exhausted beyond exhaustion, had heard me properly or where he would send the request for help.

Right now, the situation before me mattered more than anything else.

*Boom!*

The force of my leap made the high-rise building tremble—the building where the Teleportation magic circle had been installed.

As I shot through the distant sky, someone’s furious shout reached me.

“You lunatic!”

It was the Skeleton King. Using his own power, he had created wings made of bone and was approaching at high speed with powerful wingbeats.

Or he would have, if I had not blocked him.

“Go somewhere else.”

“What?”

“The range is too wide. We’ll split up and cover it.”

A Monster Wave. And it was happening in Busan, a city with an extremely high population density.

The desert or sparsely populated military zones in the footage I had seen through Magic Johnson were one thing, but here in Busan, thousands of people were packed within a radius of just a few kilometers.

I had to stop the disaster from spreading by any means necessary.

“I’ll take the bridge first. You……”

“Damn it. Got it.”

Time was short, so my words were brief, but they were enough for the Skeleton King to understand.

He swallowed hard and looked down into the dizzying depths below.

His gaze swept over the road swallowed by screams and chaos and the people running for their lives. Then it suddenly began to tremble.

“Damn it, what the hell is that now?”

“What else would it be?”

I answered shortly, pulled a spare spear from my inventory, and aimed it at the ground.

Through my greatly enhanced eyesight, it looked as grotesque as any other monster. The scales covering its entire body and the fins extending down to its jaw were repulsive.

*Merman.*

An aquatic monster that lived in an environment like the sea.

The creature had the form of a male merperson, but it was neither beautiful nor kind like the ones described in fairy tales.

The hundreds of Mermen surging out of the sea at that very moment and descending upon the people made that clear enough.

—Ssssss!

—Karruk!

The creatures charged forward, spewing unintelligible cries, barnacle-covered tridents flashing in their hands.

Beyond those flashing points sat a little girl, collapsed on the ground and crying.

“Waaaaah! Mommy!”

“Minhee!”

The child’s crying. Her parents’ screams as they turned around.

And hundreds of monsters charging toward their first prey.

*Now.*

I shifted my center of gravity.

My body, tilted diagonally as it shot through the wind, abruptly angled downward, and internal energy flowing through my dantian burst from the tips of my feet.

*Bang!*

I began a steep descent, stepping on empty air with **Stepping on Empty Air**.

But no matter how quickly I hurried, the girl would inevitably die before I arrived if things continued like this.

*Go.*

After taking a short breath, I scattered the spear I had been aiming at the ground.

*Whoooosh!*

A single spear plunged down like a bolt of lightning from an unreachable height.

Cutting through the wind, erasing space, carrying the two characters for *certain death*—

It pierced its target.

*Splurch! Crunch-crunch-crunch!*

The Merman leading the charge toward the girl, along with a dozen or so monsters around it, turned into a handful of blood.

At the same time, hundreds of Mermen stopped moving and stared up at the sky with their mouths hanging open.

Half ferocity and half confusion mixed in their eyes as I muttered:

“What are you looking at, you sons of bitches?”

*Inventory Open. Summon.*

*Click.*

The moment two spears appeared in my hands, my arms were already swinging toward the ground.

*Boom! Crack!*

Scales harder than steel shattered, and fins tore apart.

One Merman, lucky enough to lose only half its body, let out a mournful death cry.

—Krruk, krruruk!

So noisy.

*Inventory Open. Summon.*

*Whoosh! Boom!*

Around noon, with the sun high overhead, unexpected fireworks exploded.

Sticky blood trickled down the railing of the tilted Gwangan Bridge.

*More. More. One more time.*

*Open. Summon. And summon. Summon again.*

It happened in the blink of an eye. The System operated instantly, and my movements were faster than the wind and more powerful than lightning.

My hand shot out at the same moment as my thoughts, gripping dozens of spears in the span of only a few seconds before scattering them toward the ground.

*Die.*

*Whoooosh—boom-boom-boom!*

They split apart. They exploded.

Those who tried to block the spears with their tridents died together with their weapons. Those who tried to flee died before they could even take a step.

When the girl who had been crouched and crying just three meters away began to hiccup, there was nothing left around her.

“ hic. Sob.”

She looked about nine years old. Muffled by the small hands covering her mouth, sobbing hiccups escaped her.

How did I appear in those enormous eyes?

A monster that had defeated monsters? Or an angel descending from the sky?

I did not know. But one thing was certain.

*Unlike me…… you won’t have any good memories of this place.*

The aftertaste was bitter. After landing lightly on the ground, I crooked one finger instead of trying to comfort the girl.

*Shhh.*

**Seizing an Object Through Empty Space.** Qi stretched out smoothly and pushed the girl away.

Toward her parents, who were running toward her while screaming.

But that family’s misfortune was not over yet.

*Ruuuumble.*

The sea had turned black despite the shining sun.

As I stared at the *thing* concealed within another wave rising dozens of meters into the air, I lowered the tip of White Flame.
```

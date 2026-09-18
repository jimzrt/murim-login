<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0365.txt",
      "sha256": "1d26a96852abff7117152d19e78bc4069763bbb0bb125a4b350b20d32f123ea7",
      "bytes": 13442
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d91483139d045e3057e09985b997e6220b263ed8b58120e9bf37512e7b0ebcf9",
      "bytes": 2196
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "94d58cb1e53faa7d68d65d12e95dd3e435f80b87dcbcda4fd0cc28167e91e1c3",
      "bytes": 127096
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "07660c254421f9889f4edeae8bc2e90e86a043ceca0fdf92af94836a31585538",
      "bytes": 813
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8f249db2be578fb6ffa1f7b613f011bb219a4b1645138a4f204ddd0d9d28112b",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "50b92e2f3d2955bad9e0cb2ac7756cf7437965c9d2f9615cb3d77d706bf32b83",
      "bytes": 1195
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3ca29d7e2588f46300d15335ffb158bfff63b588abb210dc031b00bcdcc93601",
      "bytes": 622
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "5ef55ea527bef822a03a1173ccc4438d6fe1a7876af9b78f7b199c6424cbfb77",
      "bytes": 848
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "cbe4bf3def5f3ad3828701cdce7c6a74797d72293b325fc340d4bb162847f883",
      "bytes": 96967
    }
  ],
  "estimated_tokens": 66680
}
-->

# Durable State Update — Chapter 365

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 365. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 365. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 365,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 365,
    "continuity_sources": [365],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Jeok Cheongang has awakened after his prolonged coma but remains physically weakened and incompletely recovered.",
    "The Western Heaven Demon Lord remains alive and hostile after suffering a crushed ankle and having his wrist torn free by Jin Taekyung; their confrontation is unresolved.",
    "Jin Taekyung has reached the Supreme Peak realm through enlightenment.",
    "White Flame is in Jin Taekyung's grasp after being drawn through Seizing an Object Through Empty Space, and a fire dragon manifested from its spearhead.",
    "The Divine Physician remains alive but unconscious after the battle and has lost his dantian and martial arts.",
    "The Myriad-Poison Ring remains in Jin Taekyung's possession and cannot be appraised by the System.",
    "Cheongpung remains engaged in his confrontation with First Fiend.",
    "The underground prison remains in the process of collapsing.",
    "The Western Heaven Demon Lord serves the unidentified Lord of Heaven.",
    "The reported destruction of the Tang Clan, Qingcheng, and Emei remains unconfirmed."
  ],
  "continuity_sources": [
    364
  ],
  "open_questions": [
    "What will be the outcome of the unresolved confrontation between Jin Taekyung, Jeok Cheongang, and the Western Heaven Demon Lord?",
    "What is the full nature and purpose of the Myriad-Poison Ring?",
    "Can the Divine Physician survive after losing his dantian and martial arts?",
    "What is the actual outcome of the attacks on the Tang Clan, Qingcheng, and Emei?",
    "Can Cheongpung survive or escape his confrontation with First Fiend?"
  ],
  "safe_through": 364,
  "temporary_decisions": [
    "Render 신물 as sacred treasure.",
    "Render 이기어검 as Qi-Controlled Sword or the art of controlling a sword with qi.",
    "Render 화신귀무 as Dance of the Fire God and Demon, 겁화 as hellfire, and 초절정 as Supreme Peak.",
    "Preserve Jin Taekyung's vulgar, self-mocking voice and Jeok Cheongang's rough, profane protective voice.",
    "Use established renderings for White Flame, Seizing an Object Through Empty Space, Sword Force, Scorching Yang Qi, and underground prison."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |
| 정 소협 | **Young Hero Jeong** | Address for one injured Five Gates heir; his given name is not stated. |
| 갈 소협 | **Young Hero Gal** | Address for one injured Five Gates heir; his given name is not stated. |
| 석 모 | **Seok** | Self-identification by Honghwa Inn's chief steward; his given name is not stated. |
| 석 총관 | **Chief Steward Seok** | Title and surname form used for Honghwa Inn's chief steward. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 점소이 검신 되다 | **The Shop Assistant Becomes a Sword God** | Wuxia novel title read by Hyuk Mujin. |
| 아파야 무인이다 | **You Must Hurt to Become a Martial Artist** | Wuxia novel title read by Hyuk Mujin. |
| 무림의 아들 걸어서 구주팔황 세 바퀴 반 | **The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes** | Wuxia novel title read by Hyuk Mujin. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이 첨사 | **Assistant Commissioner Li** | Address form for Li Feng |
| 홍 내관 | **Eunuch Hong** | Eunuch and Deputy Military Commissioner of Shanxi Province |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 육합검 | **Six Harmonies Sword** | Huashan sword technique known by Cheongpung. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 상청검 | **Supreme Clarity Sword** | Huashan sword technique listed among Cheongpung's knowledge. |
| 낙화추영장 | **Falling Flower Chasing Shadow Palm** | Huashan palm technique listed among Cheongpung's knowledge. |
| 산화무영수 | **Scattering Flowers Shadowless Hand** | Huashan hand technique listed among Cheongpung's knowledge. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 근위대 갑옷 세트 | **Royal Guard Armor Set** | Armor set Li Feng offers Cheongpung. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 고평문 | **Gopyeong Sect** | Minor sect whose young sect leader is pressured by Taekyung. |
| 고평지부 | **Gopyeong Branch** | Proposed branch designation under the Jin Family of Taiyuan. |
| 상산왕의 증표 | **Prince Shangshan's Token** | Golden medallion awarded by Zhu Bao as the Quest Reward. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 금성전장 | **Golden Star Exchange** | Financial institution that issued the thousand-nyang bank draft. |
| 전표 | **bank draft** | Negotiable draft used for the thousand-silver-nyang payment. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 평양 | **Pyongyang** | City invoked in Taekyung's communist-atmosphere joke. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 비무행 | **dueling tour** | Cheongpung's planned journey to challenge the Ten Dragons and Phoenixes. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 서안 | **Xi’an** | Historic city near Huashan. |
| 서악 | **Western Peak** | Name for Huashan among the Five Great Mountains. |
| 흑사파 | **Black Serpent Sect** | Dark-path gambling-den gang in Xi’an. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 매화검수 | **Plum Blossom Swordsmen** | Huashan appointment held by its three elite disciples. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 십팔반병기 | **eighteen traditional weapons** | Training weapons displayed on a rack. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 찍고 땡 | **touch-and-go method** | Repeatedly reaching a destination and returning as an endurance exercise. |
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 진무량 | **Jin Muryang** | Founder of the Jin Family; legendary martial artist from roughly three hundred years earlier. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 태초 마을 | **Taecho Village** | Place named by Taekyung immediately after surviving the fall. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 낙안봉 | **Falling Goose Peak** | Huashan peak exceeding five hundred jang; Cheongpung climbed it as a child. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 검성 수련 간접 체험기 | **Sword Saint Training: A Secondhand Experience** | Cheongpung's Peak-grade cliff-training Quest. |
| 검성 수련 간접 체험기-2 | **Sword Saint Training: A Secondhand Experience—2** | Linked Quest generated after the first training Quest succeeds. |
| 초보 수련자 | **Beginner Trainee** | System Title upgraded after the tenth cliff climb. |
| 중급 수련자 | **Intermediate Trainee** | System Title received after Beginner Trainee is upgraded. |
| 황하방 | **Yellow River Gang** | Organization involved in a dispute with the Sogong Sect. |
| 소공문 | **Sogong Sect** | Sect involved in a dispute with the Yellow River Gang. |
| 남부상회 | **Southern Merchant Guild** | Merchant organization whose matter is reported to Jin Wikyung. |
| 내당주 | **Inner Hall Master** | Title for the head of the Jin Family's Inner Hall. |
| 내외당 | **Inner and Outer Halls** | The Jin Family's two internal administrative divisions. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 천근추 | **Thousand-Catty Drop** | Technique Cheongpung identifies when Taekyung lifts the spear shaft beneath his foot. |
| 일권복호 | **One Fist Subdues the Tiger** | Named form of the Crouching Tiger Fist. |
| 매화권 | **Plum Blossom Fist** | Huashan fist technique Cheongpung uses in sparring. |
| 천응조 | **Heavenly Eagle Claw** | Huashan claw technique used by Cheongpung. |
| 봉미혈 | **Fengwei acupoint** | Acupoint around the ribs targeted by Cheongpung. |
| 태권도 | **Taekwondo** | Martial art Taekyung practiced as a child. |
| 태극 1장부터 8장까지 | **Taegeuk Forms 1 through 8** | Standard taekwondo pattern sequence Taekyung copied as a child. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 오행매화보 | **Five-Element Plum Blossom Steps** | Footwork technique Cheongpung combines with Dark Fragrance Drift. |
| 백전백패 | **Hundred Battles, Hundred Losses** | Taekyung's proposed teasing nickname for Mujin. |
| 너구리 | **Neoguri** | Instant-noodle brand used in Taekyung's flavor joke. |
| 진라면 | **Jin Ramen** | Instant-noodle brand used in Taekyung's flavor joke. |
| 푸라면 | **Puramyeon** | Instant-noodle brand used in Taekyung's flavor joke. |
| 매화오품지 | **Plum Blossom Five-Point Finger** | Five-finger technique Cheongpung uses during the duel. |
| 벽을 넘어서 | **Beyond the Wall** | System Quest generated during Taekyung's breakthrough. |
| 절정 고수 | **Peak Master** | System class awarded after Taekyung completes Beyond the Wall. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 텡게르 | **Tengger** | Sky deity invoked by Temur. |
| 대칸 | **Great Khan** | Title of the former ruler whose descendants Temur and Chinggen claim to be. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 마유주 | **mare's-milk wine** | Fermented alcoholic drink offered at the gathering. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 흑사 | **Black Sand** | Eyepatched middle-aged leader of the Black Sand Band; a newly introduced identity. |
| 흑사대 | **Black Sand Band** | Han-Chinese mounted-bandit force of one hundred. |
| 천풍단 | **Heavenly Wind Band** | Five-hundred-member northern plateau mounted-bandit force subordinate to Black Sand. |
| 천풍단주 | **Heavenly Wind Band Leader** | Leader operating under Black Sand's orders near Datong. |
| 하곡 | **Hequ** | Route and Jin Family branch targeted as the alliance's entry point into Shanxi. |
| 참마검 | **horse-chopping sword** | Heavy saber used by the Human Butcher; rendered descriptively. |
| 삼매진화 | **Samadhi True Fire** | Internal-energy flame demonstrated by the unnamed old man. |
| 귀환자 | **Returnee** | System Title |
| 명가의 자제 | **Scion of a Prestigious Family** | System Title |
| 승부사 | **Gambler** | System Title |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 가공되지 않은 만년한철 | **Unprocessed Ten-Thousand-Year Cold Iron** | System Item |
| 장인을 찾아라 | **Find the Master Artisan** | System Quest |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 철기방 | **Ironcraft Guild** | Hubei guild composed mainly of skilled craftsmen and closely associated with the Nine Sects and One Gang. |
| 철기방주 | **Guild Leader of the Ironcraft Guild** | Title of the Ironcraft Guild’s leader; the current leader is Jang Taebo’s disciple. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 구방표국 | **Nine-Room Escort Bureau** | Escort Bureau that supplies Jang Taebo with a fifty-year-old He Shou Wu every four months. |
| 하수오 | **He Shou Wu** | Traditional medicinal herb; a thirty-year-old specimen is offered to Jang Taebo. |
| 오십 년 묵은 하수오 | **Fifty-Year-Old He Shou Wu** | First Rate Spirit Herb shown in the System Item Window; can provide up to about two years of internal energy. |
| 불로초 | **Herb of Eternal Youth** | Spirit herb said to grant eternal youth and immortality. |
| 불로초를 찾아서 | **In Search of the Herb of Eternal Youth** | System Quest generated after Jang Taebo names the Herb of Eternal Youth. |
| 천검진인 | **Heavenly Sword True Person** | Taoist-style title of the current Sect Leader of Huashan, who once commissioned a sword from Jang Taebo. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 공청석유, 용의 발톱, 여의주 구하기 | **Get Gongcheong Seokyu, a Dragon’s Claw, and a Dragon Pearl** | Quest generated after Jang Taebo makes additional demands; Taekyung rejects it. |
| 천풍 | **Heavenly Wind** | Short form displayed on the Heavenly Wind Band's flag. |
| 장팔 | **Jang-pal** | Woodcutter who meets and helps the unnamed old man. |
| 장 씨 | **Jang** | Surname form used for the woodcutter Jang-pal. |
| 장가촌 | **Jang Family Village** | Clan village where Jang-pal lives. |
| 홍가촌 | **Hong Family Village** | Clan village said to be three hundred li from Jang Family Village. |
| 신령님 | **Mountain Spirit** | Jang-pal's mistaken address for the unnamed old man. |
| 장씨 | **Jang** | Unspaced source variant of 장 씨; surname form for Jang-pal. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 백련정강 | **Baekryeon Jeonggang** | Extremely hard steel used to forge Hyuk Mujin's sword. |
| 강자지존 | **Might Makes Right** | Murim principle invoked as the basis for Mae Jonghak's challenge. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 꼰머 | **boomer-brain** | Related slang term Cheongpung says has a similar meaning. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 부마도위 | **Imperial Son-in-Law** | Imperial title mentioned by Jang Taebo. |
| 천하오대세가 | **Five Great Families** | Expanded source form of 오대세가. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 장천 | **Jangcheon** | Name Jeok Cheongang gave to the orphan who later became Jopil; means “Vast Sky.” |
| 벌모세수 | **cleansing the sinews and washing the marrow** | Jeok Cheongang’s constitution-improving technique. |
| 상단전 | **upper dantian** | Advanced dantian whose opening signifies entry into the Martial Extremity realm. |
| 무극 | **Martial Extremity realm** | Realm associated with opening the upper dantian. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 왕팔 | **Wangpal** | One of the youths who tried to take Jangcheon's dumpling. |
| 홍소칠 | **Hong Sochil** | One of the youths who tried to take Jangcheon's dumpling. |
| 소우평 | **So U-pyeong** | One of the youths who tried to take Jangcheon's dumpling. |
| 보옥 | **Treasured Jade** | Missing Fire Gate Clan treasure sought by Jeok Cheongang. |
| 우황태 | **Woo Hwangtae** | Chief of the Seongun Escort Bureau and Woo Jintae's father. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 수문위사 | **gate guard** | Jin Family guard stationed at the gate. |
| 장주 | **Lord** | Title used for one of the Five Gates heads, as in 태 장주. |
| 패화권 | **Defeated Flower Fist** | Chulwoo’s epithet. |
| 산서기협 | **Shanxi Extraordinary Hero** | Epithet mentioned among the Jin Family’s known figures; distinct source spelling from 산서괴협. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 화검봉 | **Flower Sword Phoenix** | Eunhyang’s epithet and one of the Three Plum Blossom Elites. |
| 화산말학 | **Huashan’s Last Crane** | Taekyung’s mistaken hearing of 화산일학; not a genuine epithet. |
| 매화손절 | **Plum Blossom Cutoff** | Taekyung’s mistaken hearing of 매화삼절; not a genuine title. |
| 하곡문 | **Hequ Sect** | Small sect led by Jang Se-pal. |
| 장세팔 | **Jang Se-pal** | Leader of the small Hequ Sect. |
| 양천 | **Yangcheon** | Shanxi-area location near which a small martial arts academy operates. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 집법원 | **Disciplinary Hall** | Huashan body that handles violations of sect rules. |
| 대연무장 | **Grand Training Ground** | The Jin Family's largest training ground and the site of the grand banquet. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 일장로 | **First Elder** | Title Cheol Mubaek claims within the Mount Heng Sword Sect. |
| 이대 문주 | **second Sect Leader** | Lee Seowol's succession title as the Mount Heng Sword Sect's second Sect Leader. |
| 디그다 | **Diglett** | Pokémon species used in Taekyung's analogy. |
| 닥트리오 | **Dugtrio** | Pokémon species used in Taekyung's analogy. |
| 언더아머 | **Under Armour** | Modern sportswear brand mentioned in Taekyung's joke. |
| 추도환 | **Choo Dohwan** | Level 65 Iron Blood Sect martial artist known as the Iron Fist. |
| 철권 | **Iron Fist** | Choo Dohwan's epithet. |
| 상도문 | **Sangdo Sect** | Sect pledging itself to the Jin Family at the banquet. |
| 황진수 | **Hwang Jinsu** | Level 25 challenger from Hwang Family Manor. |
| 황가장 | **Hwang Family Manor** | Family estate represented by Hwang Jinsu. |
| 갈 모 | **Gal Mo** | Nameless wandering martial artist who challenges Chulwoo. |
| 한 남자가 있어, 널 너무 사랑한 | **There Is a Man Who Loved You So Much** | System Quest title generated by Chulwoo's jealous challenge. |
| 나약한 수컷 | **Weak Male** | System Title granted if Jin Taekyung refuses the Quest. |
| 화산제일의 기재 | **Huashan’s greatest prodigy** | Reputation attributed to Baek Museong; Taekyung privately mocks the title. |
| 연쇄고백마 | **Serial Confession Man** | Taekyung's mocking description of Chulwoo after the duel. |
| 대종남파 | **Great Zhongnan Sect** | Expanded and formal reference to the Zhongnan Sect. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 육합전성 | **Six-Harmonies Voice Transmission** | Supreme Peak martial art that transmits the user's voice from every direction. |
| 천하삼십육검 | **Heavenly River Thirty-Six Swords** | Zhongnan Sect sword technique used by Song Il. |
| 열화문의 신물 | **Fire Gate Clan’s sacred treasure** | The Unnamed Sword entrusted by Jeok Cheongang to Jin Taekyung. |
| 종남산 | **Mount Zhongnan** | Mountain where the Zhongnan Sect’s main sect is located. |
| 혀왕 | **Tongue King** | Taekyung’s joking nickname for Jeok Cheongang after his verbal intimidation. |
| 피독지환 | **Poison-Averting Ring** | Clear-jade ring offered to Jeok Cheongang as a gift. |
| 마이클 천강 | **Michael Cheongang** | Taekyung’s joking nickname for Jeok Cheongang during the banquet. |
| 양천상회 | **Yangcheon Merchant Association** | Merchant association whose owner seeks Jeok Cheongang’s help with the Hebei Peng Family. |
| 철혈도 | **Iron Blood Saber** | Epithet of Peng Cheolyeong. |
| 팽철영 | **Peng Cheolyeong** | Family Head of the Hebei Peng Family and successor to the Thunderbolt Saber King. |
| 화천검 | **Fire Heaven Sword** | The true name of the former Unnamed Sword; beloved sword of the Fire Gate Clan's tenth Sect Leader. |
| 볼케이노문 | **Volcano Gate Clan** | Taekyung's joking nickname and pun for the Fire Gate Clan; not a separate sect. |
| 석가장 | **Seok Family Manor** | Prominent merchant family and estate described as foremost in the merchant world. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 아마존 | **Amazon** | Region referenced in Taekyung's crude joke. |
| 블랙 아나콘다 | **Black Anaconda** | Snake referenced in Taekyung's crude joke. |
| 악불군 | **Ak Bulgun** | Spear Instructor at Heaven's Gate Temple from the Shandong Yue Family. |
| 산동악가 | **Shandong Yue Family** | Family to which Ak Bulgun belongs. |
| 적통 | **orthodox lineage** | The legitimate succession of the Fire Gate Clan's tradition. |
| 구음절맥 | **Nine Yin Severed Meridians** | Rare severed-meridian condition caused by powerful innate yin energy and associated with an early death. |
| 닥터 최태 | **Doctor Choi Tae** | Taekyung’s joking doctor label for Jeok Cheongang. |
| 하 총관 | **Chief Ha** | Surname-and-office form; one of Seok Family Manor's five Outer Stewards. |
| 외총관 | **Outer Steward** | Senior administrative office at Seok Family Manor. |
| 일보 후퇴 | **One Step Back** | Peak-Grade Quest requiring Jin Taekyung to make Jeok Cheongang retreat one step. |
| 탄지공 | **finger-flicking technique** | Head Elder's internal-energy technique, used as a comparison for the stone projectiles. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 천룡 | **Heavenly Dragon** | The ideal form Jeok Cheongang wishes Taekyung to become. |
| 화령초 | **Fire Spirit Grass** | Scorching Yang Qi elixir consumed by Taekyung. |
| 홍화초 | **Red Flower Grass** | Scorching Yang Qi elixir consumed by Taekyung. |
| 염적초 | **Flame Red Grass** | Scorching Yang Qi elixir consumed by Taekyung. |
| 설삼 | **snow ginseng** | Elixir compared with the chapter's three selected roots. |
| 혈도 타통 | **Acupoint Opening** | System Quest created when Taekyung consumes the three elixirs. |
| 회음혈 | **Huiyin Acupoint** | Starting acupoint of the Conception Vessel; its location causes Taekyung particular danger during forced opening. |
| 임맥 타통 | **Conception Vessel Opening** | System Achievement earned after Taekyung opens the Conception Vessel. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 김종수 | **Kim Jong-su** | Jinho's college classmate who absconded with his housing deposit. |
| 제주도 | **Jeju Island** | Referenced in Taekyung's joke about Jinho being a premium-grade sucker. |
| 희망 길드 | **Hope Guild** | Guild to which Taekyung officially belongs; it provides him an officetel. |
| 양주시 | **Yangju City** | Location of the reported F-rank Gate. |
| 장흥면 | **Jangheung-myeon** | Administrative area containing Uldae-ri. |
| 울대리 | **Uldae-ri** | Village where the reported F-rank Gate appeared. |
| 노스트라다무스 | **Nostradamus** | Referenced as someone who could not predict Gate formation. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 황철수 | **Hwang Cheol Soo** | B-rank public-service Hunter and tollgate team leader. |
| 박 씨 | **Mr. Park** | Taxi driver rescued by Taekyung; surname address form. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 유시진 | **Yoo Sijin** | Captain and Team Leader of Support Team 25. |
| 유 대위 | **Captain Yoo** | Rank-and-surname form used for Yoo Sijin. |
| 김 기자 | **Reporter Kim** | Military correspondent assigned to cover the Gate incident. |
| 정 팀장 | **Team Leader Jeong** | Hunter Team Leader serving with the military support team. |
| 대위 | **captain** | Military rank held by Yoo Sijin. |
| 군종 기자 | **military correspondent** | Reporter Kim's military reporting role. |
| 수방사 | **Capital Defense Command** | Abbreviation used for 수도방위사령부. |
| 수도방위사령부 | **Capital Defense Command** | Military command to which the support team belongs. |
| 25 지원팀 | **Support Team 25** | Military and Hunter support unit at the tollgate. |
| 특전사 | **Special Forces** | Military force whose uniform is worn by one of the support-team personnel. |
| 페더 폴 | **Feather Fall** | Descent-slowing spell used by the arriving mage. |
| 그리스 | **Grease** | Spell used to make the ogres lose their footing. |
| 베르체니 | **Vercheni** | Venerable Italian artisan family commissioned to make the Peace Guild's magical equipment. |
| 이탈리아 | **Italy** | Country associated with the Vercheni artisan family. |
| 원미구 | **Wonmi-gu** | District of Bucheon shown in Taekyung's televised caption. |
| 서울 외곽 순환도로 | **Seoul Outer Ring Expressway** | Expressway whose tollgate incident made Taekyung famous. |
| 톨게이트 영웅 | **Tollgate Hero** | Media nickname given to Jin Taekyung after the tollgate incident. |
| 황소자리 | **Taurus** | Zodiac sign Song Song uses as a nickname for Taekyung. |
| 뇌이버 | **Naver** | Source-spelling variant used in Hayeon's reference to the real-time search rankings. |
| 아홉 시 뉴스 데스크 | **Nine O'Clock News Desk** | KPS live news program where Taekyung is waiting to be interviewed. |
| 한국일보 | **Korea Daily** | Daily newspaper carrying a feature on Taekyung. |
| 고려일보 | **Goryeo Daily** | Daily newspaper carrying a feature on Taekyung. |
| 행복한 생각 | **Happy Thoughts** | Publication carrying a human-interest feature on Taekyung. |
| 시사 핫 토픽 | **Current Hot Topic** | Current-affairs publication. |
| 국회 말말말 | **Parliament’s Words of the Day** | Publication covering remarks made in Parliament. |
| 자유 애국당 | **Freedom Patriot Party** | Political party whose chairman makes the quoted remark. |
| KPS | **KPS** | Broadcaster carrying the Nine O’Clock News. |
| 아홉 시 뉴스 | **Nine O’Clock News** | KPS news program Taekyung appeared on. |
| 헤일리 뉴스 | **Hailey News** | Media outlet identified in the online comments. |
| ㅂㅎㅇ | **B.H.Y.** | Initials of a Hailey News reporter; no full name is given. |
| 오마이갓 뉴스 | **Oh My God News** | News outlet approaching Taekyung in the parking garage. |
| 주부 일간지 | **Housewives’ Daily** | Daily publication represented by Reporter Hong. |
| 생생 시사 토크 | **Vivid Current-Affairs Talk** | Current-affairs talk program approaching Taekyung. |
| 피터 필립 | **Peter Philip** | Swiss watchmaker credited with making the Universe-302. |
| 유니버스-302 | **Universe-302** | Luxury automatic mechanical watch used as Choi’s deterrent. |
| 제갈량 | **Zhuge Liang** | Historical strategist invoked in Taekyung’s comparison of Choi’s cleverness. |
| 스위스 | **Switzerland** | Country associated with the watchmaker. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 스타 길드 | **Star Guild** | Guild in Incheon acquired and renamed by Won Myunghoon. |
| 주간 헌터즈 | **Weekly Hunters** | Hunter magazine carrying Taekyung's interview. |
| 벙어리 삼룡이 | **Mute Samryong** | Title character of a well-known Korean short story. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 쫄보 | **Coward** | Song associated with Won Myunghoon. |
| 헌터를 몰라 | **I Don't Know Hunters** | Song associated with Won Myunghoon. |
| 탈주 | **Escape** | Song associated with Won Myunghoon. |
| 유니콘 차트 | **Unicorn chart** | Japanese music chart mentioned in relation to Won Myunghoon. |
| 원명훈 신드롬 | **Won Myunghoon Syndrome** | Taekyung's joking name for Won's former cultural influence. |
| 도원결의 | **Peach Garden Oath** | Oath Taekyung jokes that Jinho would want the three men to swear together. |
| A급 헌터 | **A-Rank Hunter** | System Achievement and Hunter status Taekyung receives in this chapter. |
| 아이튜브 | **iTube** | Live-streaming platform hosting the Hunter Association ceremony. |
| 태경좌 | **Taekyung the Lord** | Online nickname created by viewers during Taekyung's live broadcast. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 은빛 갈기 라이칸스로프 | **Silver-Mane Lycanthrope** | Lv. 83 boss monster of The Lycanthrope’s Black Forest. |
| 라이칸스로프의 검은 숲 | **The Lycanthrope’s Black Forest** | B-rank Gate cleared in this chapter. |
| 도민수 | **Do Minsu** | A-rank star Hunter and Won Myunghoon’s close friend; died in the Myeongdong Station Mutated Gate Catastrophe. |
| 명동역 변이 게이트 대참사 | **Myeongdong Station Mutated Gate Catastrophe** | Eight-year-old Gate disaster in which Do Minsu and around thirty others died. |
| 소나무 위키 | **Sonamu Wiki** | Online wiki consulted about Won Myunghoon. |
| 종훈 | **Jonghun** | Personal name of Star Guild Team 1 Leader. |
| 블랙 와이번 | **Black Wyvern** | A-Rank Gate monster remembered by Taekyung. |
| 블랙 와이번의 둥지 | **The Black Wyvern’s Nest** | A-Rank Gate and destination of the joint raid. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 드레이크 | **Drake** | High-tier dragonkin monster. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 마지막 잎새 | **The Last Leaf** | Story referenced in Taekyung's comparison. |
| 만티코어 | **Manticore** | A-Rank Gate monster and original raid target. |
| 만티코어의 밀림 | **Manticore’s Jungle** | Original joint-raid location. |
| 예티의 목걸이 | **Yeti’s Necklace** | Cold-producing System Item lent by Won Myunghoon. |
| 한서불침 | **Unaffected by Cold and Heat** | Condition attributed to Taekyung after opening both vessels. |
| 상동역 변이 게이트 사건 | **Sangdong Station Mutated Gate incident** | Traumatic Gate incident Taekyung survived three years earlier. |
| 그린 와이번 | **Green Wyvern** | Lv. 97 A-Rank monster encountered during the joint raid. |
| 진우 | **Jinwoo** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 김종훈 | **Kim Jonghun** | Star Guild Team 1 Leader's personal name. |
| 오크 | **Orc** | Monster species. |
| 오크 워리어 | **Orc Warrior** | B-Rank Orc designation. |
| 블라디미르 스탈린 | **Vladimir Stalin** | Russian jewelry maker named by Team Leader Choi. |
| 프로즌 아이 | **Frozen Eye** | Necklace worn by Team Leader Choi. |
| 설원의 바람 | **Wind of the Snowfield** | Effect activated by Yeti's Necklace. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 북한 | **North Korea** | Country referenced in Taekyung's comparison. |
| 수령님 | **Supreme Leader** | Title used in Taekyung's North Korean TV comparison. |
| 마에스트로 | **maestro** | Conductor title used in Won's Guild-management analogy. |
| 디스패스 | **Dispass** | Celebrity-gossip site cited by Taekyung. |
| 네임드 몬스터 | **Named Monster** | Classification given to the Wyvern that killed the scouts. |
| 변이 게이트 | **Mutated Gate** | Gate classification identified at the raid site. |
| 레어 몬스터 | **Rare Monster** | Anomalously powerful monster designation introduced for monsters exceeding their expected Grade. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 힘껏 찌르기 | **Stab with All My Strength** | Taekyung’s descriptive alternate name for the spear strike he used against the Black Wyvern. |
| 김현수 | **Kim Hyunsu** | Four-month Hunter and first victim of the incident three years earlier; Taekyung’s deceased comrade. |
| 이혜림 | **Lee Hyerim** | Deceased comrade of Taekyung from the incident three years earlier. |
| 송동혁 | **Song Donghyeok** | Deceased comrade of Taekyung from the incident three years earlier. |
| 박상호 | **Park Sangho** | Deceased comrade of Taekyung from the incident three years earlier. |
| 김한웅 | **Kim Haneung** | Deceased comrade of Taekyung from the incident three years earlier. |
| 박광현 | **Park Gwanghyeon** | Deceased comrade of Taekyung from the incident three years earlier. |
| 홍천수 | **Hong Cheonsu** | Ten-year veteran Hunter and deceased comrade who saved Taekyung from goblins. |
| 기의 발현 | **Manifestation of Qi** | System Achievement completed by Taekyung. |
| 백독불침 | **Unaffected by a Hundred Poisons** | System effect granted to Taekyung's body. |
| 에어 브레스 | **Air Breath** | Unique dragonkin ability used by Carus. |
| 힐 | **Heal** | Healing spell cast by Carus. |
| 슬로우 | **Slow** | Spell cast five times in succession by Carus. |
| 카루스 | **Carus** | Name of the Black Wyvern. |
| 외눈박이 | **One-Eyed** | Epithet of Carus, who has only one eye. |
| 다크 바인딩 | **Dark Binding** | Spell cast by Carus. |
| 매직 애로우 | **Magic Arrow** | Spell cast by Carus. |
| 속박 마법 | **Binding Magic** | System description of Carus's thorny-vine spell. |
| 마비 독 | **Paralysis Poison** | Poison carried by Carus's binding vines. |
| 신경 독 | **Nerve Poison** | Poison carried by Carus's binding vines. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 네임드 몬스터 처치 | **Named Monster Defeated** | Achievement granted for killing Carus. |
| 파이어 레인 | **Fire Rain** | A-Rank mage spell used by Butler Kim. |
| 개보린 | **Dogvorin** | Taekyung's dog-themed pun on Gevorin, a Korean painkiller. |
| 대법원 | **Supreme Court** | Court invoked in Won Myunghoon's metaphor for an irreversible verdict. |
| 어스퀘이크 | **Earthquake** | Named spell cast by Butler Kim. |
| 헌터TV | **HunterTV** | Major Hunter-focused cable channel that conducts the exclusive live broadcast. |
| 합스부르폰 가 | **Hapsburphon family** | Long-established German family of equipment makers. |
| PSV-96K | **PSV-96K** | Concealed camera that evades detection magic and functions in unstable-Gate mana. |
| 검찰 | **prosecutors’ office** | Government prosecutorial institution that summons and investigates Taekyung. |
| 법무부 | **Ministry of Justice** | Government ministry whose Hunters could have accompanied the prosecutor. |
| 대한제국 | **Korean Empire** | Historical-era reference used in Taekyung’s joke. |
| 크리스티 | **Christie’s** | Auction house whose appraisers valued Carus’s remains. |
| 소더비 | **Sotheby’s** | Competing major auction house. |
| 고조선TV | **GojoseonTV** | Television outlet that reports the Christie’s auction. |
| 카타르 | **Qatar** | Country of Prince Cheonsur. |
| 천수르 | **Cheonsur** | Qatar’s prince who wins the auction for Carus’s remains. |
| 박형석 | **Park Hyeongseok** | Online commenter who identifies himself during the argument. |
| 낙양 | **Luoyang** | Historic city in Henan Province and the chapter’s setting. |
| 하남성 | **Henan Province** | Province containing Luoyang. |
| 회면 | **huimian noodles** | Famous Henan noodle dish served at the inn; explained in a footnote. |
| 백주 | **baijiu** | Strong distilled liquor ordered at the inn. |
| 동천파 | **Dongcheon Sect** | Long-established dark-path faction ruling Luoyang’s nights. |
| 동천방 | **Dongcheon Gang** | Source variant used in the description of Heukgeol’s epithet. |
| 흑걸 | **Heukgeol** | Lower-ranking Dongcheon Sect officer known as its lone beast. |
| 궁소 | **Gungsu** | Dark-path swordsman killed during the Dongcheon Sect’s initial attack. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 독룡파 | **Poison Dragon Sect** | Dark-path faction mentioned as a possible origin of the monk. |
| 흑혈문 | **Black Blood Sect** | Dark-path faction mentioned as a possible origin of the monk. |
| 나한권 | **Arhat Fist** | Shaolin martial art used by Unnamed. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 소실봉 | **Shaoshi Peak** | Peak of Mount Song that must be climbed to reach the Shaolin Abbot. |
| 지객당 | **Guest Reception Hall** | Shaolin area where visitors without a specific purpose must remain. |
| 관세음보살 | **Avalokiteshvara** | Buddhist invocation shouted by Unnamed during his attack. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 계율원 | **Discipline Hall** | Shaolin disciplinary office that urges Hong Dao to return to a formal residence. |
| 녹옥불장 | **Green Jade Buddha Staff** | Ancient Shaolin sacred treasure carried by Hong Dao. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 태양권 | **Solar Fist** | Martial art mentioned in Taekyung's joke about Unnamed's forehead strike. |
| 천년독각사 | **Thousand-Year Poison Horned Snake** | Extremely venomous horned snake used to make Hong Dao's thirty-year-old liquor. |
| 비선 | **Hidden Thread** | Secret intelligence network and its chief hidden informant serving the Family Head. |
| 소선 | **Lesser Threads** | Informants operating beneath the Hidden Thread. |
| 황산파 | **Huangshan Sect** | Prestigious sect that has already collapsed. |
| 산주 | **Mountain Lord** | Anhui title for Jeok Cheongang as master of Mount Jiuhua. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 남궁룡 | **Namgung Ryong** | Family Head of the Namgung family. |
| 은형술 | **concealment technique** | Peak-level technique used by the Hidden Thread to erase his presence. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 수혈 | **Sleep Acupoint** | Acupoint whose successful strike prevents the target from resisting sleep. |
| 천급 | **Heaven-grade** | Highest classification in the Namgung family's intelligence system. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 화왕 특제 금제단 | **Fire King's Special Restriction Pill** | System consumable that suppresses internal energy and reduces three physical stats for one week. |
| 화왕의 불지옥 수련-1 | **Fire King's Inferno Training-1** | Nonrefusable training Quest created when Jeok blasts Taekyung from the summit. |
| 화왕의 지옥불 수련-1 | **Fire King's Hellfire Training-1** | Source-title variant used for the completed Quest. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 만년 한철 | **Ten-Thousand-Year Cold Iron** | Spaced source variant for the chain material. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 화왕의 지옥불 수련-2 | **Fire King's Hellfire Training-2** | System Quest completed after the waterfall training. |
| 요지부동 | **Unmoving** | Achievement earned after the waterfall training. |
| 맷집 | **Toughness** | System attribute that changes into Endurance. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 권각 수련 | **Fist-and-Foot Training** | Repeat Quest for basic fist-and-foot exercises. |
| 권각술 | **fist-and-foot martial arts** | Unlearned martial-arts category referenced by the System. |
| 열화동 | **Fire Gate Cavern** | Ancestral cavern where the Fire Gate Clan began and its legacy continues. |
| 열화의 계승자 | **Heir of the Fire Gate** | Quest generated when Jeok begins passing on the Fire Gate Clan's inheritance. |
| 문방사우 | **Four Treasures of the Study** | The brush, inkstone, ink, and paper used for calligraphy and painting. |
| 한림학사 | **Hanlin Academician** | Scholarly office used in Wipeng's teasing comparison. |
| 대화백 | **master painter** | Title used jokingly for an accomplished painter. |
| 해동 | **Haedong** | Traditional name for Korea. |
| 칠로군 | **Seven-Route Army** | Seven-pronged force led by Wipeng and the Jin Dragon Squad. |
| 황금 씨족 | **Golden Clan** | Traditional name for the ruling lineage descended from the khans. |
| 합비 | **Hefei** | City on the Jin Family's new escort-trade route. |
| 진가표국 | **Jin Family Escort Bureau** | New name for the former Seongun Escort Bureau under the Jin Family. |
| 잠룡출사 | **The Sleeping Dragon Enters Service** | Title of Jin Wikyung's planned painting. |
| 검미새 | **sword nut** | Taekyung's joking term for someone obsessed with swords. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 헨젤과 그레텔 | **Hansel and Gretel** | Fairy-tale siblings used in Taekyung's chained-iron-ball joke. |
| 남궁옥 | **Nangong Ok** | Namgung Ryong's only son, the Nangong Family's Lesser Family Head and the Sword Dragon. |
| 검룡 | **Sword Dragon** | Epithet of Nangong Ok; one of the Ten Dragons and Phoenixes. |
| 제왕검형 | **Emperor's Sword Form** | Sword form invoked by the Azure Sky Sword King. |
| 삼초살 | **Three-Move Kill** | Sudden Quest requiring Taekyung to withstand three moves. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 오기조원 | **Five Qi Returning to Origin** | High martial realm displayed by Jeok Cheongang. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 대성 | **Great Completion** | Completion stage of a martial technique. |
| 흑산채 | **Black Mountain Stronghold** | Bandit organization on a major route between Henan and Anhui. |
| 흑종필 | **Heuk Jongpil** | Leader of Black Mountain Stronghold. |
| 금와상단 | **Geumwa Merchant Group** | Merchant group targeted by Black Mountain Stronghold. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 묘안석 | **cat’s-eye stone** | Valuable stone used as an example of a profitable haul. |
| 성마대연 | **Demonic Grand Banquet** | Hypothetical banquet the Demonic Cult would hold if the Central Plains Murim had lost. |
| 여아홍 | **Yeoahong** | Traditional Chinese rice wine; literally Daughter's Red. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 적살부 | **Red-Killing Axe** | Epithet of Heuk Jongpil. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 개봉 | **Kaifeng** | City where the preliminary competition will be held. |
| 섬 | **seom** | Traditional Korean measure of rice. |
| 종리추 | **Jongni Chu** | Young Peak martial artist from Yunnan; conceals his sect. |
| 상승검 | **Always-Victorious Sword** | Jongni Chu's self-styled epithet, coined in this chapter. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 마이클 존슨 | **Michael Johnson** | False name Taekyung gives Jongni Chu. |
| 호철 | **Hocheol** | Jin Dragon Squad martial artist and Hyuk Mujin's subordinate. |
| 간장 | **Gan Jiang** | Legendary swordsmith named in comparison with Mo Ye. |
| 막야 | **Mo Ye** | Legendary swordsmith named in comparison with Gan Jiang. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 풍운전신 | **Wind-and-Cloud War God** | Jeok Cheongang's mistaken version of Gong Iljung's title. |
| 정력도왕 | **Virility Saber King** | Jeok Cheongang's insulting replacement title for the Thunderbolt Saber King. |
| 하북 팽가 | **Hebei Peng Family** | Family of the Thunderbolt Saber King. |
| 하북제일미 | **Hebei's greatest beauty** | Description of the Thunderbolt Saber King's great-grandson's wife. |
| 참회동 | **Repentance Cave** | Zhongnan Sect place of penance. |
| 철수신룡 | **Iron-Water Divine Dragon** | Title of Cheol Soo, a member of the Ten Dragons and Phoenixes. |
| 도곤 | **Dogon** | Title for a Peak-level gambler. |
| 곽철융 | **Kwak Cheolyung** | One of the three legendary Dogons. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 짝귀 | **Jjak-Gwi** | Legendary Dogon from Guangdong. |
| 노르웨이 | **Norway** | Taekyung's temporary nickname for the huge foreign-looking applicant. |
| 호접문 | **Butterfly Sect** | Sect of the eliminated martial artist Jangyu. |
| 장유 | **Jangyu** | Martial artist eliminated during the fist-and-foot assessment. |
| 소당문 | **Sodang Sect** | Sect of the martial artist Gobul. |
| 고불 | **Gobul** | First Rate martial artist who passes the fist-and-foot assessment. |
| 장보고 | **Jang Bogo** | Historical Korean maritime commander used in Taekyung's joke about the Seafaring King. |
| 화왕의 분노 | **Fire King's Wrath** | Failure penalty for the Star-Array Grand Banquet Quest. |
| 파선권 | **Ship-Breaking Fist** | Named fist technique demonstrated by the Iron-Water Divine Dragon. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 서역 | **Western Regions** | Region from which the glasses were imported. |
| 청성산 작두 | **Qingcheng Mountain Guillotine** | Epithet of the unnamed martial artist who cut off A-Gwi's wrist. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 곤륜운룡 | **Kunlun Cloud Dragon** | Epithet of a Kunlun Sect young prodigy. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 혼뢰각 | **Hunroe Leg** | Epithet of the Guangxi Peak master specializing in leg techniques. |
| 신기묘룡 | **Divine Marvel Dragon** | Epithet of the Zhuge Clan's Lesser Family Head. |
| 금면공자 | **Gold-Faced Young Master** | Title of the unnamed gambler who bet on Taekyung. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 낭왕 | **Wave King** | One of the Ten Kings; already deceased. |
| 나한동 | **Arhat Cave** | Shaolin cave where Unnamed is preparing. |
| 항룡십팔장 | **Eighteen Dragon-Subduing Palms** | Beggars' Sect martial art mentioned by Gung Gibang. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 유비 | **Liu Bei** | Historical ruler in the Three Visits to the Thatched Cottage allusion. |
| 삼고초려 | **Three Visits to the Thatched Cottage** | Allusion Zhuge Gyun uses to justify choosing the third option. |
| 천마신교 | **Heavenly Demon Divine Cult** | The Demonic Cult's self-styled formal name. |
| 흑수표 | **Black Water Dart** | Epithet of Taekyung's defeated main-event opponent. |
| 운룡대팔식 | **Cloud-Dragon Eight Forms** | Baek Woo's Kunlun movement technique. |
| 오태식 | **Oh Tae-sik** | Taekyung's joking alternate name for the Cloud-Dragon Eight Forms. |
| 권기 | **Fist Energy** | Projected martial energy produced by a fist technique. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 연명검 | **Life-Sustaining Sword** | Nickname earned by Jongni Chu for repeatedly winning by a narrow margin. |
| 무적신검 | **Invincible Divine Sword** | Epithet of Zhuge Gyun's unidentified opponent. |
| 강풍 | **Kang Pung** | False name Cheongpung uses while disguised as the Invincible Divine Sword. |
| 암중살 | **Shadow Killer** | The Hidden Shadow Pavilion's finest agent. |
| 태원박가 | **Taiyuan Park Family** | Fabricated family identity Taekyung uses to bait Cheongpung. |
| 호남성 | **Hunan Province** | Province mentioned during Cheongpung's account of his travels. |
| 혼원도 | **Hunyun Saber** | Epithet of the Hebei Peng Family’s eldest grandson, defeated by Jin Taekyung in the quarterfinals. |
| 유운신룡 | **Willow-Cloud Divine Dragon** | Wudang direct disciple and Cheongpung’s quarterfinal opponent. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 승패병가지상사 | **Victory and defeat are simply part of war** | Common saying Jeok Cheongang uses while taunting the Thunderbolt Saber King. |
| 송문고검 | **Pine-Pattern Ancient Sword** | Willow-Cloud Divine Dragon’s sword. |
| 태청검법 | **Great Clarity Sword Technique** | Wudang sword technique used by the Willow-Cloud Divine Dragon. |
| 태극혜검 | **Taiji Wisdom Sword** | Wudang’s supreme sword technique. |
| 매화삼십육검 | **Thirty-Six Plum Blossom Swords** | Huashan sword technique used by Cheongpung. |
| 타구봉법 | **Dog-Beating Staff Technique** | Beggars’ Sect staff technique. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 극상승의 안법 | **ultimate eye technique** | Advanced visual technique Cheongpung learned from Mae Jonghak. |
| 허초 | **feint** | Deceptive attack Jongni Chu says he used against Cheongpung. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 좌장 | **presiding chair** | Authority overseeing the Star-Array Grand Banquet. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천산산맥 | **Tianshan Mountains** | Mountain range associated with the Demonic Cult. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 팔 성 | **eighth stage** | Current stage of Taekyung's Qi Sense Skill. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 심사관 | **Judge** | Official supervising the Star-Array Grand Banquet duels. |
| 화륜각 | **Flame Wheel Kick** | Taekyung's blue-flame kicking technique. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 사량발천근 | **Four Ounces Deflecting a Thousand Catties** | Principle Jongni Chu cites for redirecting force rather than opposing it directly. |
| 만리추행 | **Myriad-Mile Pursuit** | Epithet of the Beggars' Sect Leader and master of movement techniques. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 명문혈 | **Mingmen acupoint** | Acupoint into which Jeok Cheongang sends internal energy while treating Hong Dao. |
| 석가 | **Shakyamuni** | Buddhist figure invoked by Hong Dao in his earlier conversation with Jeok Cheongang. |
| 한수 | **Han Su** | Scholar-like Dark Heaven operative who kills a Hidden Shadow Pavilion messenger. |
| 염호 | **Flame Tiger** | Red-bearded Dark Heaven operative and Han Su's longtime friend. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 굉천 | **Hongcheon** | Hong Dao's youngest Junior Brother; Supreme Peak Shaolin master defending the temple. |
| 백중 | **Baekjung** | Traditional Buddhist observance during which the Shaolin attack occurs. |
| 오악 | **Five Sacred Mountains** | Mountain grouping that includes Mount Song. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 백보신권 | **Hundred-Step Divine Fist** | Hongcheon's named martial art. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 음양쌍괴 | **Yin-Yang Twin Freaks** | Shared epithet of Flame Tiger and Han Su. |
| 범공 | **Beomgong** | Dharma name of a Shaolin monk killed by Han Su during the Great Faction War. |
| 면벽동 | **Face-Wall Cave** | Shaolin cave where Unnamed is located. |
| 음귀 | **Yin Ghost** | Han Su's epithet. |
| 사대금강 | **Four Great Vajras** | Four elite Shaolin martial monks killed by Han Su. |
| 장경각 | **Scripture Depository** | Shaolin repository whose martial arts manuals the attackers intend to burn. |
| 살문 | **Killing Gate** | Command given while the Hundred and Eight Arhats Formation is deployed. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 백팔나한 | **Hundred and Eight Arhats** | Shaolin's elite formation unit of 108 martial monks. |
| 백팔나한진 | **Hundred and Eight Arhats Formation** | Formation used by the Hundred and Eight Arhats. |
| 폭혈마공 | **Exploding Blood Demonic Art** | Demonic art used by masked attackers as a battlefield self-detonation technique. |
| 부동심 | **Unshakable Mind** | Mental discipline Hongcheon is accused of abandoning when he loses composure. |
| 음한지공 | **Yin-Cold Technique** | Han Su's extreme cold-based internal technique. |
| 삼도천 | **Sanzu River** | Buddhist river associated with the boundary between life and death; footnote on first use. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 진천뢰 | **Heaven-Shaking Thunder** | Powerful gunpowder explosive named in the Blood Lord's false threat to lure Hong Dao away. |
| 사성 | **Four Saints** | Rank the Blood Lord says Jeok Cheongang might have attained if the Great Faction War had continued another year. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 천독마군 | **Heaven-Poison Demon Lord** | Archfiend of the Heavenly Demon Divine Cult and former second-in-command of the Demonic Cult. |
| 혈귀검마 | **Blood Ghost Sword Demon** | Title Song Ho mistakenly attributes to Mae Jonghak before recognizing him as Jongni Chu. |
| 태원 진가 | **Jin Family of Taiyuan** | Source-spaced form of the Jin Family's name. |
| 토토 | **Toto** | Gambling or lottery reference contrasted with Dodo in Taekyung's joke. |
| 낙양괴의 | **Luoyang Strange Physician** | Renowned Central Plains physician; eccentric and fiercely temperamental, he examined Jeok Cheongang. |
| 염왕채 | **Yama's Debt** | Taekyung's joking term for a ruinous loan or loan-shark debt. |
| 골렘 | **Golem** | Magical rock-based monster classification. |
| 스톤 골렘 | **Stone Golem** | A-rank stone-bodied monster faced by the rookie Hunters. |
| 아이언 골렘 | **Iron Golem** | Higher-ranking golem type appearing in a group after the Stone Golem raid. |
| 헤이스트 | **Haste** | Buff spell cast by Song Song. |
| 스트렝스 | **Strength** | Strength-enhancing buff spell cast by Song Song. |
| 힐링 | **Healing** | Healing spell cast by Song Song. |
| 파이어 월 | **Fire Wall** | Fire spell cast by Butler Kim. |
| 내가중수법 | **Inner-Family Heavy Hand** | Taekyung's joking comparison for his mother's painful palm strike. |
| 모친신장 | **Mother's Palm Strike** | Taekyung's humorous name for the beating delivered by his mother. |
| 국정원 | **NIS** | South Korea's National Intelligence Service, mentioned in Taekyung's joke. |
| 노재헌 | **No Jaehun** | Middle-school student from the adjacent class, remembered as tall and boastful about working out. |
| 선웅제 | **Seon Woongje** | Taekyung's middle-school classmate who fought with No Jaehun. |
| 한국대 | **Hankuk University** | Short form for the country's most prestigious university; Jihoon's university. |
| 한국대학교 | **Hankuk University** | Full form of the university attended by Jihoon. |
| 게이트 관리청 | **Gate Management Agency** | Agency that provides Taekyung's VIP limousine. |
| 8학군 | **School District 8** | Prestigious Gangnam education district associated with affluent families and elite schools. |
| 김진수 | **Kim Jinsoo** | Peace Guild rookie who graduated first in the training camp’s B-rank course. |
| 블랙 헌터 | **Black Hunter** | Unregistered Awakened person who has received systematic training comparable to a Hunter. |
| 미등록자 | **unregistered Awakened person** | Awakened person who fails to register with the Association within the designated period. |
| 특수 치료 병동 | **Special Treatment Ward** | Hospital ward where healers, rather than ordinary doctors, treat severe injuries. |
| 통합당 | **United Party** | Political party identified in the article about Yoon Seoyoon. |
| 윤서윤 | **Yoon Seoyoon** | United Party Supreme Council member and assemblywoman named in a political article. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 임영준 | **Im Yeongjun** | Level 95 A-rank Black Hunter concealed as a rural resident. |
| 세 얼간이 | **Three Idiots** | Taekyung's mocking collective nickname for three acquaintances. |
| 멸천신권 | **Heaven-Destroying Divine Fist** | Taekyung's full-power fist technique used to destroy the mansion's defensive barriers; distinct from 멸염신권. |
| 한남동 | **Hannam-dong** | District where Park Tae Seop's mansion is located. |
| 11팀 | **Team 11** | Myeongdong Guild's officially nonexistent team of Black Hunters. |
| 김철수 | **Kim Cheol Soo** | C-rank junior Hunter in Myeongdong Guild's Security Team. |
| 1팀 | **Team 1** | Myeongdong Guild's elite team. |
| 이민수 | **Lee Minsu** | C-rank Hunter in Myeongdong Guild's Security Team; distinct from Kim Minsu. |
| 김 실장 | **Manager Kim** | Park Tae Seop’s security manager; his phone is used by Choi Minwoo. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 어른폰 | **AdultPhone** | Taekyung’s Korean pun on iPhone; retain the child/adult explanation in a footnote. |
| 행신동 불닭볶음손 | **Haengsin-dong Fire-Chicken Stir-Fried Hand** | Taekyung's former nickname for his painful hand strike; the translation preserves the buldak-bokkeum-myeon/son pun. |
| 산군 | **mountain lord** | Traditional epithet for a tiger; retain an explanatory footnote on first use. |
| 석 팀장 | **Team Leader Seok** | Lee Jungryong's security-team leader and direct Disciple. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 소영 | **Soyeong** | Team Leader Choi's deceased mother and Cheon Taemin's daughter. |
| 슬레이어 | **Slayer** | Cheon Taemin's title after killing the Demon King. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 한강 | **Han River** | River associated with the bridge-collapse incident Lee Jungryong recalls. |
| 마포대교 | **Mapo Bridge** | Bridge that collapsed when Kim Hwajong saved Lee Jungryong eighteen years earlier. |
| 비급제작 | **Martial Arts Manual Creation** | System Skill for creating martial arts manuals; requires at least 300 sheets of A4 paper. |
| 마나 연공법 | **Mana Cultivation Method** | Modern Hunter cultivation method recognized by Team Leader Choi and Butler Kim. |
| 고양진가 | **Jin Family of Goyang** | Taekyung's joking modern-world counterpart to the Jin Family of Taiyuan. |
| 2차 각성자 | **Second Awakener** | Hunter classification for someone who has awakened a second time. |
| 진기도인 | **True Qi Guidance** | System-named method for guiding another person's internal energy. |
| 소주천 | **Small Circulation** | Circulation of qi according to the Jin Family's Cultivation Technique. |
| 일주천 | **complete circulation** | Completion of one full qi circulation. |
| 등짝, 등짝을 보자! | **Back, Back—Let's See Your Back!** | Peak-grade repeat Quest title. |
| 난 소화한 공력의 반만 가져가 | **I'll Take Only Half the Internal Energy I Digest** | Sudden Quest title generated in Team Leader Choi's dantian. |
| 백년설삼 | **Hundred-Year-Old Snow Ginseng** | Elixir whose undigested internal energy remained in Taekyung's dantian. |
| 삼화취정 | **Three Flowers Gather at the Crown** | Near-completed phenomenon associated with entering the Supreme Peak realm. |
| 무아지경 | **Trance** | State Taekyung briefly enters during the energy digestion. |
| 내가고수 | **I'm a Master** | System Title granted to Taekyung. |
| 이순신 | **Admiral Yi Sun-sin** | Historical admiral invoked in Taekyung's comparison. |
| 명량대첩 | **Battle of Myeongnyang** | Historical naval victory used in Taekyung's comparison. |
| 수련자 | **Trainee** | System Title replaced in this chapter. |
| 훈련 교관 | **Training Instructor** | System Title awarded after several trainees reach One Star. |
| 킹태경 | **King Taekyung** | Online nickname praising Taekyung. |
| 로그인 무림 | **Login Murim** | Web novel recommended in the Hunter community comments. |
| 제로빅 | **Zerobic** | Name used in a forum joke about the recommended web novel. |
| 둘리 | **Dooly** | Korean cartoon character referenced in the goodwill proverb. |
| 흑마법사의 검은 숲 | **Black Wizard’s Black Forest** | A-rank Gate ruled by a black wizard or necromancer. |
| 게이트 공략 | **Gate Raid** | Quest automatically generated upon entering the Gate. |
| 흑마법사 | **black wizard** | Ruler or magical classification associated with the Gate. |
| 네크로맨서 | **necromancer** | Alternate description of the black wizard ruling the Gate. |
| 도사견 | **Tosa mastiff** | Taekyung’s nickname for the veteran third-week trainees. |
| 댕댕이 | **pup** | Taekyung’s nickname for first-day trainees. |
| 피리 부는 사나이 | **the Pied Piper** | Nickname for Taekyung when he lures monsters toward the Guild formation. |
| 구울 | **Ghoul** | Undead monster species. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 좀비 | **Zombie** | Undead monster species. |
| 언데드 몬스터 | **Undead Monster** | Classification for the cursed dead in the Gate. |
| 스켈레톤 솔져 | **Skeleton Soldier** | Skeleton subtype. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 워리어 | **Warrior** | Skeleton subtype mentioned alongside Soldiers and Mages. |
| 스켈레톤 나이트 | **Skeleton Knight** | A-rank undead monster that commands lower-level skeletons. |
| 골검 | **Bone Sword** | Sword wielded by the Skeleton Knights. |
| 스켈레톤 워로드 | **Skeleton Warlord** | Level 105 undead monster created when the leading Skeleton Knight transforms. |
| 정몽주 | **Jeong Mong-ju** | Historical Korean scholar-official referenced through the Warlord’s quotation. |
| 단심가 | **Song of My Single Heart** | Poem associated with Jeong Mong-ju and unwavering loyalty. |
| 통합 언어 팩 | **Unified Language Pack** | System function that lets Taekyung understand demon-world speech. |
| 서울지부 협회장 | **Seoul Branch President** | Hunter Association official overseeing the rescue response at the Black Forest. |
| 서울 협회장 | **Seoul Branch President** | Source variant for the Seoul Branch President. |
| 스켈레톤 아처 | **Skeleton Archer** | Skeleton subtype defeated during the Warlord's EXP harvest. |
| 서울 중앙 협회장 | **Seoul Branch President** | Hunter Association official who delayed the rescue response and authorized the Peace Guild's entry. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 이우중 | **Lee Woojoong** | Seoul Branch President of the Hunters Association. |
| 서울 중앙지부 헌터 협회장 | **Seoul Branch President** | Source title for Lee Woojoong; variant of the established Seoul Association title. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 소르코바체 | **Sorkovache** | Russian furniture master credited with making Team Leader Choi's seventeenth-century-style imperial sofa. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 코난 | **Conan** | Host of the American talk show discussing Taekyung's viral interview. |
| 워로드몬 | **Warlordmon** | Taekyung's mocking nickname for the Skeleton Warlord. |
| CNM | **CNM** | American broadcaster requesting an interview with Taekyung. |
| BCC | **BCC** | British broadcaster offering Taekyung a live special-guest interview. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 몸통박치기 | **Body Slam** | Comic attack command Taekyung gives Warlordmon. |
| 수능 | **college entrance exam** | National university entrance examination taken by Hayeon. |
| 내신 | **school grades** | School-record grades referenced in Taekyung’s insult. |
| 파블로프 | **Pavlov** | Reference to Pavlov’s dogs. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 몬스터 웨이브 | **Monster Wave** | Catastrophic release of monsters when Gate mana exceeds its capacity. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 공안 무력부 | **Public Security Armed Forces Division** | Chinese state Hunter force deployed against the Monster Wave. |
| 오성홍기 | **Five-Starred Red Flag** | China's national flag. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 난충시 | **Nanchong City** | City near the disaster site shown in the reconnaissance footage. |
| 중화인민공화국 | **People's Republic of China** | Formal country name shouted by the Chinese Hunters. |
| 중앙위원회 총서기 | **General Secretary of the Central Committee** | Office held by Xiao Yang. |
| 빙빙 | **Bingbing** | Name or nickname of the child in the Monster Wave footage. |
| 샤오 양 | **Xiao Yang** | General Secretary of China's Central Committee who specifically requests Taekyung's participation. |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 대통령 | **President** | Title for Korea's head of state. |
| 대통령 각하 | **Mr. President** | Formal address for the President. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 중국 공산당 | **Chinese Communist Party** | China's ruling political party. |
| 중국 중앙위원회 | **China's Central Committee** | Chinese Communist Party leadership body referenced in the crisis response. |
| 중앙 군사 위원회 | **Central Military Commission** | Chinese military leadership body that requested Lee Jungryong's participation. |
| 인민해방군 | **People's Liberation Army** | Chinese military deployed to seal off the catastrophe area. |
| 주한 중국 대사 | **Chinese ambassador to Korea** | Diplomatic representative who met Lee Jungryong secretly. |
| 포케불프 | **Focke-Wulf** | German aircraft manufacturer. |
| 종석이 아저씨 | **Chairman Jongseok** | Taekyung's joking misrendering of Chairman Xiao Yang's title and name. |
| 보잉 747-8 VIP | **Boeing 747-8 VIP** | Chinese private jet used for the Sichuan response. |
| 중국 중앙 위원회 | **China's Central Committee** | Source-spaced variant of the established Chinese Central Committee title. |
| 첫이슬 후레쉬 | **First Dew Fresh** | Soju brand served aboard the private jet. |
| 청두 | **Chengdu** | Administrative capital of Sichuan Province and destination airport city. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 국제 게이트 연구소 | **International Gate Research Institute** | Research body studying the increase in Gate mana. |
| 게이트 마력 급증 조사 결과 | **Investigation Results: Sudden Increase in Gate Mana** | Title displayed on Choi Minwoo's tablet. |
| 도쿄핫 | **Tokyo Hot** | Adult-video studio referenced in Taekyung's insult; footnoted. |
| 도쿄루 | **Tokyo-ru** | Red-light establishment referenced in Taekyung's joke. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 키라라 | **Kirara** | Worker at Tokyo-ru referenced in Taekyung's joke. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 의선 | **Medicine Immortal** | Alternate sobriquet for the Divine Physician. |
| 홍길동 | **Hong Gil-dong** | Legendary Korean outlaw invoked in Taekyung's joke about the Divine Physician. |
| 오씨 | **Oh** | Surname form used in the clue identifying the Luoyang Strange Physician. |
| 오배자 | **Chinese gallnut** | Medicinal ingredient named in the Divine Physician's clue. |
| 신 서방 | **Mr. Shin** | Name form used in the System Quest targeting the Divine Physician. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 국자감 | **Guozijian** | The empire's highest educational institution. |
| 제갈공후 | **Zhuge Gonghu** | Former Murim Alliance Chief Strategist and deceased member of the Ten Kings. |
| 팽 | **Peng** | Surname form for the Thunderbolt Saber King, Peng Cheolhu. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 주호군 | **Ju Hogun** | Ju Hwaran's father and former leader of the Yongbong Escort Bureau. |
| 석 표두 | **Chief Escort Seok** | Yongbong Escort Bureau Chief Escort and the thirty-third casualty of the current escort journey. |
| 총 표두 | **Chief Escort** | Senior escort-bureau office held by Heo Jun. |
| 만리추풍신법 | **Myriad-Li Chasing Wind Movement Technique** | Beggars' Sect movement technique known for speed. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 쟁자수 | **caravan porter** | Porters who lead the escort caravan's horses and carts. |
| 녹림도 | **Green Forest bandit** | Bandit belonging to the Green Forest Alliance. |
| 흑석산 | **Black Stone Mountain** | Mountain named for its black stones and located on the route to Mount Zhongnan. |
| 흑석채 | **Black Stone Stronghold** | A powerful Green Forest Alliance stronghold led by Heavenly Axe. |
| 십팔채 | **Eighteen Strongholds** | Short form for the Green Forest Alliance's eighteen major strongholds. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 노필중 | **Noh Piljung** | Middle-aged escort captain and member of the Dragon-Phoenix Three Escorts. |
| 미향이 | **Mihyang** | Yongbong Escort Bureau maid who relayed rumors about Song Ilseom. |
| 용봉삼표 | **Dragon-Phoenix Three Escorts** | Collective title for the Yongbong Escort Bureau's three outstanding escort captains. |
| 천년설삼 | **Thousand-Year Snow Ginseng** | Secret Zhongnan Sect cargo; a fully digested specimen can grant a full jiazi of internal energy. |
| 유엽도 | **willow-leaf saber** | Saber wielded by Song Ilseom. |
| 살인멸구 | **Silencing the Witnesses** | Killing witnesses to prevent a secret from being exposed. |
| 방열 | **Bangyeol** | Personal name of Heavenly Axe; Level 93 Peak master and leader of Black Stone Stronghold. |
| 버뮤다 삼각지대 | **Bermuda Triangle** | Taekyung's joking collective label for the three companions descending the hill. |
| 용봉표국의 위기 | **Crisis of the Yongbong Escort Bureau** | Sudden Quest accepted and completed by Taekyung. |
| 천력부 처치 | **Defeat Heavenly Axe** | Quest objective completed when Taekyung kills Bangyeol. |
| 흑석채 제압 | **Subdue Black Stone Stronghold** | Quest completed when the surviving bandits surrender. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 서안루 | **Xi'an Tower** | Prominent pleasure house in Xi'an. |
| 백 씨 | **Baek** | Surname form used when Baek Museong introduces himself. |
| 종남일룡 | **Zhongnan One Dragon** | Epithet of Hyuk Sopyung. |
| 화종지회 | **Huashan–Zhongnan gathering** | Gathering where Baek Museong and Hyuk Sopyung met ten years earlier. |
| 종남 제일의 기재 | **Zhongnan Sect’s greatest prodigy** | Reputation attributed to Hyuk Sopyung. |
| 일인전승 비인부전 | **one-person transmission and refusal to teach the unworthy** | Fire Gate Clan transmission principle. |
| 육체파 | **physical school** | Taekyung’s joking self-description. |
| 봉수 | **Bong-su** | Zhongnan Sect Disciple and Hyuk Sopyung’s same-generation Junior Brother. |
| 태을검대 | **Taeeul Sword Unit** | Elite Zhongnan Sect force composed of second-generation Disciples. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 송 총관 | **Manager Song** | Xi’an Tower chief manager, identified by surname. |
| 사백 | **Senior Martial Uncle** | Zhongnan Sect title used for a senior of the speaker’s Master’s generation. |
| 둘째 사백 | **Second Martial Uncle** | Hyuk Sopyung’s designation for the Senior Martial Uncle currently in Xi’an. |
| 호접지몽 | **Butterfly Dream** | Allusion to Zhuangzi’s dream of becoming a butterfly. |
| 귀식대법 | **Turtle Breath Technique** | Cheongpung’s joking description of breath-holding and suspended bodily functions. |
| 귀신대법 | **Ghost Technique** | Taekyung’s pun on Turtle Breath Technique after Mujin appears dead. |
| 심폐소생권 | **Cardiopulmonary Resuscitation Fist** | Taekyung’s humorous name for the palm strike used to revive Mujin. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 주공산 | **Ju Gongsan** | Former head and founder of the Yongbong Escort Bureau. |
| 광동진가 | **Guangdong Chen Family** | Family whose last child Ju Gongsan carried to Henan during the Great Faction War. |
| 십만마병 | **hundred thousand demonic soldiers** | Army fielded by the Demonic Cult during the Great Faction War. |
| 광동 | **Guangdong** | Province under Demonic Cult control during the war. |
| 광동성 | **Guangdong Province** | Source form specifying Guangdong as a province. |
| 강서 | **Jiangxi** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 섬서성 | **Shaanxi Province** | Source form specifying Shaanxi as a province. |
| 유니세프 | **UNICEF** | Organization referenced in Taekyung's joke about Ju Hogun's charity. |
| 등왕루 | **Tengwang Pavilion** | Famous teahouse on the western edge of Xi'an. |
| 종남제일검 | **The First Sword of Zhongnan** | Epithet of the Taeeul Merciless Sword. |
| 철관음 | **Tieguanyin** | Tea savored by Hwangbo Eom. |
| 황보엄 | **Hwangbo Eom** | Personal name of the Taeeul Merciless Sword. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 태을신공 | **Taeeul Divine Technique** | Zhongnan cultivation technique; Hwangbo Eom had mastered eight-tenths of it at Hyuk Sopyung's age. |
| 종화지회 | **Huashan–Zhongnan gathering** | Source spelling variant of 화종지회 for the ten-year gathering between the two sects. |
| 스피드 개건 | **Speed Beggar** | Jin Taekyung's joking label for Gung Gibang. |
| 성수장가 | **Seongsu Jang Family** | Prestigious medical family in Shandong. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 동량지재 | **pillar of Huashan** | Reputation attributed to Baek Museong. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 방자전 | **Bangjajeon (The Servant)** | Korean film title used in Taekyung's pun on insolence. |
| 종남제일인 | **Zhongnan's greatest master** | Taekyung's description of Hwangbo Eom. |
| 서안 분타주 | **Xi'an Branch Leader** | Unnamed Beggars' Sect official heading the Xi'an branch. |
| 초코파이 | **Choco Pie** | Snack brand used in Taekyung's pun on 정. |
| 흑걸개 | **Heukgeol Beggar** | Three-knot disciple and head of the Beggars' Sect's Xi'an branch; title-form of Heukgeol. |
| 왕코 | **Big Nose** | Gung Gibang's nickname for his childhood friend Heukgeol. |
| 삼결제자 | **three-knot disciple** | Beggars' Sect rank held by Heukgeol. |
| 팔결제자 | **eight-knot disciple** | Beggars' Sect rank and mark held uniquely by the Successor Beggar. |
| 법개 | **Law Beggar** | Beggars' Sect authority who enforces the sect rules. |
| 용두방주 | **Dragon-Head Gang Leader** | Leader of the Beggars' Sect and Gung Gibang's Master. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 하오문도 | **Lower District Sect member** | Member of the Lower District Sect. |
| 금오상단 | **Geumo Merchant Guild** | Merchant guild named in the evidence concerning the Yongbong Escort Bureau; source spelling distinct from 금와상단. |
| 황철심 | **Hwang Cheolsim** | Zhongnan lay disciple who secretly intervened in the Yongbong Escort Bureau's failed transaction. |
| 장문령부 | **Sect Leader's Command Token** | Copper token carrying the Zhongnan Sect Leader's authority. |
| 태을분광검 | **Taeeul Light-Dividing Sword** | One of the Zhongnan Sect's celebrated ultimate sword techniques. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 수강 | **Palm Force** | Force generated through a palm technique. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 반고 | **Pangu** | Primordial giant from Chinese creation mythology. |
| 화룡조 | **Fire Dragon Claw** | Taekyung's claw technique. |
| 벽운천강수 | **Blue Cloud Heavenly Force Palm** | Zhongnan Sect palm technique used by Hwangbo Eom. |
| 태을무형검 | **Taeeul Formless Sword** | Hwangbo Eom's supreme sword art of invisible attacks. |
| 십구 대 계승자 | **nineteenth successor** | Taekyung's Fire Gate Clan succession title. |
| 황천 | **Hwangcheon** | Second-generation Zhongnan disciple and Commander of the Taeeul Sword Unit. |
| 광룡 | **Mad Dragon** | Taekyung's joking alternative to Fire Dragon after he beats Hwangbo Eom. |
| 낙천 상단 | **Nakcheon Merchant Guild** | Merchant guild involved in a contract cancellation attributed to Zhongnan in the investigation. |
| 석도민 | **Seok Domin** | Escort Captain who died during the current Yongbong Escort Bureau mission. |
| 길왕준 | **Gil Wangjun** | Escort who died during the current Yongbong Escort Bureau mission. |
| 홍석정 | **Hong Seokjeong** | Escort who died during the current Yongbong Escort Bureau mission. |
| 노두삼 | **Noh Dusam** | Escort who died during the current Yongbong Escort Bureau mission. |
| 석삼 | **Seok Sam** | Caravan porter who died during the current Yongbong Escort Bureau mission. |
| 몽혼제 | **mind-clouding drug** | Narcotic that clouds the mind and induces sleep. |
| 낭중지추 | **needle in a bag** | Idiom meaning exceptional talent eventually reveals itself. |
| 송표산 | **Song Pyosan** | Song Ilseom's father. |
| 여사 | **Lady** | Taekyung's joking sobriquet for Kim Jeonghee. |
| 만리표 | **Ten-Thousand-Mile Escorts** | The Escort King’s famed escort missions. |
| 검동 | **sword boy** | Young attendant hired by wandering martial artists to carry swords and perform dangerous errands. |
| 만천화우 | **Rain of Ten Thousand Flowers** | Named technique invoked jokingly for rice sprayed from Gung Gibang’s mouth. |
| 송옥 | **Song Yu** | Ancient Chinese poet invoked in Gung Gibang’s beauty boast. |
| 피카소 | **Picasso** | Modern painter invoked in the comparison for Gung Gibang’s face. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 함양 | **Xianyang** | City Song Ilseom plans to visit for Ju Hogun’s elixir. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 광안 | **Guang'an** | Sichuan location where the party boards Mu Song's ship. |
| 황태구 | **Hwang Tae-gu** | Former Sichuan river-bandit power displaced by Mu Song; mastermind of the attack. |
| 어인 유술 해류 한 팔 업어치기 | **Fish-Man Jujutsu: Current—One-Arm Shoulder Throw** | Taekyung's joking name for the combined maneuver he performs with Mu Song. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 인의대협 | **Great Hero of Benevolence and Righteousness** | Flattering epithet Mungyeong uses for Mu Song. |
| 맹규 | **League regulations** | Rules of the Yangtze River Channel League. |
| 본단 | **League headquarters** | The League headquarters to which Hwang Tae-gu will be transported. |
| 기해혈 | **qi-sea acupoint** | Acupoint at the dantian whose destruction releases stored internal energy. |
| 화타 | **Hua Tuo** | Historical physician invoked in Taekyung's comparison for Mungyeong's future medical skill. |
| 당가타 | **Tang Family Hill** | The Tang Clan's former main base, burned during the Great Faction War. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 오성 | **Oseong** | One half of the paired Joseon-era names used in Taekyung's joke. |
| 한음 | **Haneum** | One half of the paired Joseon-era names used in Taekyung's joke. |
| 외당 | **Outer Hall** | The Tang Clan's outer hall area. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 가주전 | **Family Head's Hall** | Hall where the Tang Family Head receives visitors. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok. |
| 당사문 | **Tang Taesang** | Former Family Head of the Sichuan Tang Clan and Poison King; Tang Sadok’s father. |
| 미산 | **Meishan** | Sichuan location chosen as Tang Taesang’s retirement place. |
| 월영살곡 | **Moonshadow Assassination Valley** | Assassin organization whose master is said to have killed three Supreme Peak masters. |
| 곡주 | **Valley Master** | Title of the leader of Moonshadow Assassination Valley. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 사면령 | **amnesty decree** | Decree that ended the Slaughter Saint’s status as an enemy of all Murim. |
| 신의의 증표 | **Divine Physician’s Token** | Jade shard containing the clue about Sichuan’s Chinese gallnuts. |
| 삼국지 | **Romance of the Three Kingdoms** | Classic historical novel referenced in Taekyung's comparison. |
| 촉나라 | **Shu** | Kingdom referenced in the Romance of the Three Kingdoms comparison. |
| 청성산 | **Mount Qingcheng** | Mountain containing the Qingcheng Sect. |
| 아미산 | **Mount Emei** | Mountain associated with the Emei Sect. |
| 상청궁 | **Shangqing Palace** | Qingcheng Sect hall where major sect matters are decided. |
| 청풍고검 | **Cheongpung the Ancient Sword** | Alias of the Qingcheng Sect's Sect Leader; distinct from Cheongpung. |
| 청성 칠십이검자 | **Qingcheng Seventy-Two Swordsmen** | Qingcheng Sect group of First Rate masters. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 원균 | **Won Gyun** | Personal name of the City Lord of Sichuan Province. |
| 진가상단 | **Jin Family Trading Company** | Commercial organization belonging to the Jin Family of Taiyuan. |
| 애향이 | **Aehyang** | Personal name of the Sichuan City Lord's favorite concubine. |
| 묘령 | **Myoryeong** | Dharma name of the middle-aged Emei nun. |
| 묘령사태 | **Venerable Myoryeong** | Honorific form for the injured Emei nun. |
| 경천신니 | **Heaven-Shaking Venerable Nun** | Former Emei Sect Leader and sole Supreme Peak master; killed on Mount Emei. |
| 혈나찰 | **Blood Rakshasa** | Demonic Cult epithet for the Heaven-Shaking Venerable Nun during the Great Faction War. |
| 흑수인 | **Black Hand Seal** | Evil technique causing Myoryeong's progressive, potentially fatal injury. |
| 기문진 | **Mystic Gate Formation** | Formation concealing Dong Feng's clinic in Sichuan. |
| 기환노사 | **Master of Strange Illusions** | Ancient formation master who installed the hidden formation. |
| 동봉 | **Dong Feng** | Personal name of the Divine Physician and Mungyeong's Master. |
| 동 노인 | **Old Man Dong** | Address form requested by Dong Feng. |
| 오행 | **Five Elements** | Five elemental energies whose balance governs the body. |
| 음양 | **Yin and Yang** | Paired energies whose harmony has been disrupted in Jeok Cheongang. |
| 음한지기 | **Yin-Cold Qi** | Cold-aligned energy required in the treatment elixir. |
| 영약 찾아 삼만리 | **Thirty Thousand Li in Search of an Elixir** | Nonrefusable Chain Quest for the required elixir. |
| 심마니 | **Mountain Herb Gatherer** | Achievement earned after obtaining the Thousand-Year Snow Ginseng. |
| 한빙지 | **Cold-Ice Land** | Exceptionally cold valley within the Mystic Gate Formation. |
| 초상비 | **Flying Over Grass** | Movement feat performed by Dong Feng without touching the ground. |
| 답설무흔 | **Treading Snow Without a Trace** | Comparable movement feat that leaves no footprints on snow. |
| 등평도수 | **Rising on Duckweed, Crossing Water** | Comparable movement feat for walking across water. |
| 한빙지 약초 노예 | **Herb Slave of Cold-Ice Land** | Nonrefusable Chain Quest requiring the collection of medicinal herbs. |
| 한빙초 | **Cold-Ice Herb** | Medicinal herb gathered in Cold-Ice Land. |
| 지옥에서 살아 돌아온 심마니 | **Mountain Herb Gatherer Who Returned Alive from Hell** | Achievement awarded for completing the Cold-Ice Land herb collection. |
| 활신대법 | **Life-Restoring Great Technique** | Technique for regulating qi and untangling disrupted qi and blood. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 녹영대 | **Green Shadow Squad** | Sichuan Tang Clan unit specializing in intelligence and assassination. |
| 익산 | **Yishan** | Sichuan location named in Tang Sadok's deployment report. |
| 삼합 | **Sanhe** | Sichuan location named in Tang Sadok's deployment report. |
| 대사천당문 | **great Sichuan Tang Clan** | Exalted form of the Sichuan Tang Clan. |
| 당미미 | **Tang Mimi** | Name Tang Sadok gave to his Thousand-Year Poison Horned Snake. |
| 미미쨩 | **Mimi-chan** | Affectionate form used for Tang Mimi. |
| 궁 노인 | **Old Man Gung** | Hunched caretaker of the Sichuan Tang Clan's underground prison. |
| 천력마 | **Heavenly Power Demon** | Formerly imprisoned Tang Clan criminal; distinct from 천력부, Heavenly Axe. |
| 회오리치기 | **Whirlwind** | Technique Mimi-chan performs at Cheongpung's command. |
| 한빙석 | **Cold-Ice Stone** | Special stone provided by Tang Sadok for Jeok Cheongang's treatment. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 기련삼괴 | **Qilian Three Fiends** | Three identical brothers from the Qilian Mountains. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 난화수 | **Chaotic Flower Hand** | Cheongpung's technique for redirecting an opponent's force. |
| 천하일단 | **One Cut Under Heaven** | Powerful supreme form of the Thirty-Six Plum Blossom Swords. |
| 매화삼릉검 | **Plum Blossom Three-Ridge Sword** | Sword technique used by Cheongpung. |
| 채양보음 | **harvesting yang to replenish yin** | Technique mentioned as having been used to drain vitality from the Tang Clan's direct line. |
| 대천마신교 | **Great Heavenly Demon Divine Cult** | Formal historical name used by the Heavenly Power Demon for the Demonic Cult. |
| 신교 | **Divine Cult** | Short form used by the Divine Cult's members for the Heavenly Demon Divine Cult. |
| 본교 | **Divine Cult** | Self-referential form meaning the speaker's own Divine Cult. |
| 음양쌍귀 | **Yin-Yang Twin Ghosts** | Source spelling for the pair otherwise associated with the Yin Ghost and Yang Ghost. |
| 양귀 | **Yang Ghost** | Shortened counterpart to the established Yin Ghost. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 검남춘 | **Jiannan Chun** | Sichuan liquor offered to the Heavenly Power Demon. |
| 신천지 | **Shincheonji** | Modern Korean religious organization referenced in Taekyung's comparison. |
| 병 신천지 | **Sick Shincheonji** | Taekyung's joking name for a hypothetical Shincheonji splinter faction. |
| 삼결 제자 | **Three-knot Disciple** | Source-spaced form of the Beggars' Sect rank. |
| 이결 제자 | **Two-knot Disciple** | Beggars' Sect rank held by Jang Il. |
| 일결 제자 | **One-knot Disciple** | Beggars' Sect rank held by Jang Il's junior companions. |
| 부 분타주 | **Vice Branch Leader** | Office Jang Il attained in the Chengdu branch. |
| 장일 | **Jang Il** | Twenty-five-year-old two-knot Beggars' Sect Disciple killed near Emei. |
| 금당 | **Golden Hall** | Location near Chengdu where the Green Shadow Squad discovered the disguised attackers. |
| 경월년 | **Gyeongwol Year** | Historical year designation in the Tang Clan's past. |
| 당전고 | **Tang War Drum** | War drum sounded to mobilize the Tang Clan. |
| 당문고 | **Tang Clan drum** | Source spelling variant for the Tang Clan's war drum. |
| 당문십기 | **Tang Clan's Ten Wonders** | Ten Tang Clan members renowned for their martial strength. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 삼당 | **Three Divisions** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 일괴 | **First Fiend** | The Qilian Three Fiend leading the Dark Heaven assault on the Sichuan Tang Clan. |
| 이괴 | **Second Fiend** | One of the Qilian Three Fiends assigned to Qingcheng. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 만독진 | **Myriad-Poison Formation** | Tang Clan defensive formation. |
| 초대받지 않은 손님 | **Uninvited Guest** | System Quest title. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 당진후 | **Tang Jinhu** | Tang Clan direct descendant, retired Supreme Peak master, and Head Elder. |
| 천독객 | **Heaven-Poison Wanderer** | Tang Jinhu's epithet. |
| 우모침 | **ox-hair needle** | Extremely fine Tang Clan hidden weapon. |
| 피독주 | **poison-warding pearl** | Poison-neutralizing artifact carried by the black-clad attackers. |
| 단혼사 | **Soul-Severing Thread** | Tang Jinhu's silver-thread hidden weapon. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 장로원 | **Council of Elders** | Tang Clan body headed by Tang Jinhu. |
| 당휘 | **Tang Hwi** | Tang Clan martial artist named during the assault. |
| 당문삼기 | **Tang Clan's Three Skills** | Western Heaven Demon Lord's mocking replacement for Tang Clan's Ten Wonders. |
| 귀옥지 | **Ghost Prison Finger** | Eighth-stage finger technique used by the Western Heaven Demon Lord. |
| 유성추월검 | **Meteor Chasing the Moon Sword** | Named sword technique used by Cheongpung. |
| 호교사자 | **Protector of the Divine Cult** | One of four senior protectors serving the Divine Cult's Cult Leader. |
| 교주 | **Cult Leader** | Leader of the Divine Cult. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 심맥 | **heart meridian** | Meridian severed by an infiltrator to commit suicide. |
| 사혈 | **lethal acupoint** | An acupoint whose strike can kill. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 흑혈검법 | **Black Blood Sword Technique** | Sword technique restricted to Dark Heaven martial artists. |
| 권강 | **Fist Force** | Qi force projected through the Western Heaven Demon Lord's fist. |
| 후발선제 | **Striking Second, Hitting First** | Principle describing the Western Heaven Demon Lord's counterattack. |
| 맞고 뒈져라 신공 | **Get Hit and Fucking Die Technique** | Taekyung's joking name for his initial spear strike. |
| 흡정대법 | **Essence-Siphoning Great Technique** | Technique the Western Heaven Demon Lord suspects Taekyung used on the prisoners. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 청계천 | **Cheonggyecheon** | Stream invoked in Taekyung's joke about Dark Heaven. |
| 흑룡갑 | **Black Dragon Armor** | Defensive armor worn beneath the Western Heaven Demon Lord's yellow robe. |
| 사대마군 | **Four Great Demon Lords** | Collective title for the four senior Demon Lords. |
| 흡정마공 | **Essence-Siphoning Great Technique** | Source variant for the established essence-siphoning martial art. |
| 격체전공 | **Transmitting Internal Energy Across the Body** | Technique for transferring internal energy between bodies. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 스탯 포인트 | **Stat Points** | Points retained from Jin Taekyung's Level Ups. |
| 이어타정 | **carp-leaping maneuver** | Acrobatic movement Jin Taekyung uses to rise after bending backward. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 법화 | **Lotus Sutra** | Buddhist scripture used in the comparison for the Demon Lord's fiend-like face. |
| 이기어검 | **Qi-Controlled Sword** | Technique used by the Western Heaven Demon Lord to control and attack with a sword through qi. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho | casual-but-junior | Spoken 형 may stay hyung; narration uses Jinho. Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 갈 소협 | 정 소협 | fellow_Five_Gates_heir | Young Hero Jeong | formal-polite | The unnamed heir addresses the other injured heir by surname and honorific. |
| 정 소협 | 갈 소협 | fellow_Five_Gates_heir | Young Hero Gal | formal-polite | The unnamed heir responds using the other injured heir's surname and honorific. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 홍 내관 | 이풍 | political_rivals | Assistant Commissioner Li | mock-friendly and probing | Uses 우리 이 첨사 and a superficially familiar tone while testing and provoking Li Feng. |
| 이풍 | 홍 내관 | political_rivals | Eunuch Hong / Deputy Military Commissioner | formal but sarcastic | Alternates between the official title and Eunuch Hong to mock his demand for familiarity. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 공일혁 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | condescending and dismissive | Uses 후배님 while ordering Taekyung to move aside. |
| 진태경 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | polite but firm | Uses 선배님 while intervening on Cheongpung's behalf. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 공일혁 | 홍진 | junior_official_guest_to_senior_official | Deputy Military Commissioner | formal and deferential | Appeals to Hong Jin for his view on the impending disturbance. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 홍진 | 공일혁 | political_host_to_guest | Great Hero Gong | polite but cutting | Hong Jin uses the respectful title while dismissing Gong Ilhyuk and exposing his poor judgment. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 철우 | 백무성 | junior_disciple_to_senior_brother | Senior Brother | deferential | Uses 대사형 while answering Baek Museong. |
| 은향 | 백무성 | junior_disciple_to_senior_brother | Big Brother; Senior Brother | familiar and casual-polite | Repeatedly calls him 큰 오라버니 even after he insists on 대사형. |
| 홍가 | 장칠득 | older_martial_artist_to_junior_martial_artist | Little Brother Jang | familiar and casual | Hong calls Childeuk 장 아우 after inviting him to address Hong as hyung. |
| 장칠득 | 홍가 | junior_martial_artist_to_older_martial_artist | hyung | deferential, then familiar | Childeuk initially uses Senior and then adopts Hong's requested 형님 address. |
| 장칠득 | 진태경 | servant_to_third_young_master | Third Young Master | formal-deferential | Jang Childeuk addresses Taekyung as 삼공자님 while asking permission to report the dangerous training. |
| 유생 | 진위경 | scholar_to_lesser_family_head | Lesser Family Head | formal-deferential | The scholar reports matters to Jin Wikyung and apologizes for his inadequate proposal. |
| 진위경 | 유생 | lesser_family_head_to_scholar | you | formal-but-familiar | Jin Wikyung uses 자네 while correcting and instructing the inexperienced scholar. |
| 위팽 | 유생 | senior_retainer_to_scholar | you | familiar and probing | Wipeng uses 자네 while asking the scholar for his assessment. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 테무르 | 인도 | hostile_strangers | you Han Chinese bastard | hostile and contemptuous | Temur insults the seated Han Chinese man before attempting to draw his curved saber. |
| 인도 | 테무르 | intimidating_rival_to_chieftain | friend | cold and taunting | The Human Butcher calls Temur a slow friend after forcing him to sit. |
| 인도 | 흑사 | rival_power_to_rival_power | Black Sand | blunt and familiar | Uses 흑사 while cutting off Black Sand's joking introduction. |
| 흑사 | 인도 | rival_power_to_rival_power | you | playful and taunting | Teases the Human Butcher about being called a butcher without showing fear. |
| 흑사 | 칭겐 | alliance_recruiter_to_recruited_chieftain | Chinggen | lightly teasing and probing | Identifies Chinggen by name while commenting on his composure and perceptiveness. |
| 흑사 | 노인 | subordinate_to_overwhelming_unknown_master | Elder, then big brother; both rejected | deferential and fearful | Black Sand first uses 어르신 and then 형님 while trying to placate the old man; the old man rejects both forms. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |
| 장태보 | 항아 | elder_neighbor_to_child | Hanga | familiar and instructive | Calls the neighboring boy by name while correcting his speech and sending him home after dark. |
| 항아 | 장태보 | child_to_elder_neighbor | Grandpa | childlike-familiar | Repeatedly calls Jang Taebo 할부지. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 혁무진 | 항아 | visiting_adult_to_local_child | little one | coaxing and encouraging | Questions Hanga with an artificially kind smile and offers two food bundles. |
| 진태경 | 장태보 | younger_visitor_to_elder_master | Elder | polite and persistent | Taekyung repeatedly addresses Jang Taebo as 어르신 while requesting his assistance. |
| 장태보 | 진태경 | elder_master_to_younger_visitor | you | gruff and familiar | Jang Taebo uses 자네 while questioning and dismissing Taekyung. |
| 장태보 | 혁무진 | elder_smith_to_young_martial_artist | you / wet-behind-the-ears brat | gruff and insulting | Insults Mujin after Mujin whispers that Jang is senile. |
| 장태보 | 청풍 | elder_smith_to_young_martial_artist | you / lunatic | gruff and incredulous | Initially treats Cheongpung as a lunatic despite recognizing him as Mae Jonghak's disciple. |
| 장팔 | 노인 | stranger_to_elder | Mountain Spirit, then Elder | deferential and apologetic | Jang-pal initially mistakes the old man for a mountain spirit, then shifts to a respectful elder address. |
| 노인 | 장팔 | strangers | you | gruff and familiar | The old man uses 자네 while questioning Jang-pal and accepting his help. |
| 항아 | 노인 | child_to_elder_stranger | Grandpa | childlike-familiar | Hanga calls the unnamed old man 할부지 after he arrives at her family’s home; this is distinct from her address to Jang Taebo. |
| 적천강 | 장태보 | strangers; visiting elder to local smith | Old Man Jang | blunt and familiar | Uses 장 노인 while confirming Jang Taebo’s identity. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 장천 | 적천강 | disciple_to_master | Master | deferential and pleading | Jangcheon repeatedly begs Jeok Cheongang to accept him as his Disciple. |
| 적천강 | 장천 | master_to_disciple | you / fool | blunt and gruff | Jeok rejects Jangcheon’s pleas, questions his choices, and threatens to send him down the mountain. |
| 우황태 | 송 문주 | fellow_Five_Gates_head | Sect Leader Song | sharp and defensive | Uses 송 문주 while defending his need to apologize for Woo Jintae. |
| 우황태 | 태 장주 | fellow_Five_Gates_head | Lord Tae | sharp and defensive | Uses 태 장주 while arguing that retreating would damage the Seongun Escort Bureau's standing. |
| 우황태 | 거한 | insulted_stranger_to_accidental_bystander | you ox-headed bastard | aggressive and insulting | Escalates from demanding an apology to insulting the huge Huashan junior after the dropped pill. |
| 백무성 | 철우 | senior_disciple_to_second_junior_disciple | Second | calm and admonishing | Baek Museong uses 둘째 while ordering Chulwoo to stop and later directs him to find Eunhyang. |
| 진위경 | 백무성 | host_to_visiting_martial_artist | Young Hero Baek | formal-polite | Uses 백 소협 when asking whether anything is wrong. |
| 은향 | 철우 | younger_female_disciple_to_older_fellow_disciple | Senior Brother Chul | familiar and casual-polite | Uses 철 오라버니 while teasing and speaking familiarly to Chulwoo. |
| 우황태 | 철우 | insulted_stranger_to_accidental_bystander | Young Hero Chul; Great Hero Chul | apologetic and pleading | Switches from 철 소협 to 철 대협 while apologizing after Chulwoo mocks him. |
| 철우 | 우황태 | stranger_to_stranger | Brother over there | casual-polite and teasing | Uses 형장 while selecting Woo Hwangtae to guide him to a supposed scenic privy. |
| 철우 | 진태경 | stranger_to_stranger | Brother over there | casual-polite | Uses 형장 when stopping after seeing Taekyung near the mountainside. |
| 위팽 | 철우 | Jin Family retainer to visiting martial artist | Defeated Flower Fist | formal-commanding | Uses Chulwoo's epithet while stopping the fight and rebuking both men for disgracing their schools. |
| 진태경 | 철우 | rival_companions | next mountain man | casual-teasing | Taekyung responds to Chulwoo's insult with a mocking counter-insult. |
| 백무성 | 진태경 | senior_martial_artist_to_younger_martial_artist | Young Hero Jin | formal-polite | Baek Museong agrees with Taekyung while correcting Chulwoo. |
| 백무성 | 청풍 | Martial_Nephew_to_Martial_Uncle | Martial Uncle | formal-deferential | Baek formally identifies himself as Cheongpung's Martial Nephew. |
| 공일혁 | 노호검객 | junior_disciple_to_sect_elder | Elder | deferential | Gong Ilhyuk repeatedly addresses the Roaring Fury Swordsman as 장로님 while steering him toward the Jin Family. |
| 철우 | 청풍 | junior_disciple_to_Martial_Uncle | Martial Uncle | apologetic and deferential | Initially calls Cheongpung Young Hero, then recognizes him and apologizes for failing to recognize the senior sect relation. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |
| 공야청 | 진태경 | survivor_guardian_to_benefactor | Young Hero Jin | formal-polite | Gong Yacheong greets Taekyung as 진 소협 after returning to the Jin Family. |
| 소율 | 진태경 | child_survivor_to_benefactor | Uncle | childlike-familiar | Soyul repeatedly calls Taekyung 아저씨 while asking to see him. |
| 청풍 | 백무성 | Martial_Uncle_to_Martial_Nephew | Martial Nephew | affectionate-casual | Cheongpung accepts Baek Museong's apology by calling him 사질. |
| 진태경 | 백무성 | junior_martial_artist_to_Huashan_elite | Young Hero Baek | formal-polite | Taekyung addresses Baek Museong as 백 소협 while asking to change seats. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |
| 진위경 | 철우 | Jin_Family_host_to_visiting_martial_artist | Defeated Flower Fist | formal-familiar | Wikyung uses Chulwoo's epithet while asking Taekyung why he is acting strangely. |
| 진위경 | 추도환 | banquet_host_to_visiting_challenger | Young Hero Choo | formal-polite | Wikyung uses 추 소협 while accepting Choo Dohwan's request for a duel. |
| 백무성 | 진위경 | visiting_martial_artist_to_lesser_family_head | Great Hero Jin | formal-polite | Baek Museong uses 진 대협 while urging Jin Wikyung to stop the duel. |
| 청풍 | 철우 | martial_uncle_to_martial_nephew | Martial Nephew Chulwoo | affectionate-casual | Cheongpung addresses Chulwoo as his Martial Nephew while assessing Taekyung's speed. |
| 하급 무인 | 진태경 | junior_martial_artist_to_Third_Young_Master | Third Young Master | formal-deferential | The low-ranking gate martial artist uses the family title while reporting Taekyung's victory. |
| 하급 무인 | 혁무진 | subordinate_to_captain | Captain | deferential | The low-ranking gate martial artist addresses Hyuk Mujin while discussing the celebration and visitors. |
| 진위경 | 송일 | Jin Family host to visiting Zhongnan Elder | Senior | formal and guarded | Jin Wikyung respectfully asks Song Il's name before the dispute escalates. |
| 백무성 | 송일 | junior Huashan disciple to Zhongnan Elder | Senior Song | formal-deferential | Baek Museong introduces himself as a junior of Murim and pays respects. |
| 송일 | 백무성 | Zhongnan Elder to younger Huashan elite | Huashan's Lone Crane | condescending and dismissive | Song Il questions Baek Museong's identity and belittles his martial standing. |
| 백무성 | 공일혁 | senior martial artist to hostile Zhongnan junior | Great Hero Gong | formal but admonishing | Baek warns Gong Ilhyuk to watch his words after Gong threatens Taekyung. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 종남삼수 | 노호검객 | junior_Zhongnan_martial_artists_to_sect_elder | Elder | fearful-deferential | The Three Hands of Zhongnan plead with Song Il after he blames them for his humiliation. |
| 노호검객 | 공일혁 | Zhongnan_elder_to_junior_martial_artist | worthless piece of trash | furious and contemptuous | Song Il blames Gong Ilhyuk for inciting the confrontation and threatens him. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 적천강 | 악불군 | protective elder to outsider touching Taekyung | Take your hand off what’s mine | blunt and threatening | Jeok interrupts Ak Bulgun when he places a hand on Taekyung's shoulder; this does not confirm Taekyung as his Disciple. |
| 악불군 | 적천강 | junior_martial_artist_to_legendary_master | Great Hero Jeok | formal-deferential | Ak Bulgun addresses Jeok Cheongang respectfully while explaining Heaven's Gate Temple's offer. |
| 악불군 | 진태경 | academy_instructor_to_young_martial_artist | Young Hero Jin | formal-polite | Ak Bulgun repeatedly addresses Taekyung as 진 소협 while discussing the academy opportunity and apologizing after Jeok's declaration. |
| 진위경 | 하 총관 | host_to_merchant_representative | Chief Ha | formal-polite | Jin Wikyung addresses Seok Family Manor's Outer Steward by surname and office. |
| 하 총관 | 진위경 | merchant_representative_to_lesser_family_head | Lesser Family Head | deferential | Chief Ha repeatedly addresses Jin Wikyung as 소가주님 while seeking cooperation and a favor. |
| 악불군 | 진위경 | visiting_instructor_to_lesser_family_head | Lesser Family Head | formal and blunt | Ak Bulgun uses 소가주 while asking why Jin Wikyung summoned him and warning him about Heaven's Gate Temple's regulations. |
| 진위경 | 악불군 | host_to_visiting_instructor | Sir Ak | formal-polite | Jin Wikyung welcomes Ak Bulgun, explains Jin Mukyung's refusal to return, and personally delivers the Heaven's Gate Temple letter. |
| 진태경 | 악불군 | young_martial_artist_to_Heaven's_Gate_Instructor | Sir Ak | formal-polite | Taekyung addresses Ak Bulgun as 악 대협 while asking why he remains at the Jin Family. |
| 진태경 | 박 씨 | Hunter passenger to taxi driver | Sir | polite-commanding | Taekyung orders Mr. Park to flee and warn others after the Gate opens. |
| 박 씨 | 진태경 | taxi driver to passenger | passenger | startled-polite | Mr. Park recognizes Taekyung as the Hunter passenger who rescued him. |
| 김 기자 | 유시진 | military_correspondent_to_captain | Captain Yoo | formal and familiar | Calls him 유 대위님 while greeting him at the incident scene. |
| 김 기자 | 정 팀장 | reporter_to_hunter_team_leader | Team Leader Jeong | familiar and teasing | Greets him as 정 팀장 and complains about his prickly response. |
| 정 팀장 | 김 기자 | hunter_team_leader_to_military_correspondent | Reporter Kim | blunt and irritated | Says he was avoiding Reporter Kim and criticizes his excitement over the scoop. |
| 유시진 | 정 팀장 | captain_to_support_team_leader | Team Leader Jeong | blunt-commanding | Uses 정 팀장아 while questioning him about the relative severity of the two Gate incidents. |
| 유시진 | 김 기자 | captain_to_military_correspondent | Reporter Kim | formal and admonishing | Uses 김 기자님 while warning him to behave appropriately at the accident scene. |
| 김 기자 | 진태경 | reporter_to_hunter_subject | Hunter Jin Taekyung | formal and probing | Uses 진태경 헌터님 while confirming Taekyung's identity and questioning his rank. |
| 임꺽정 | 최 팀장 | guild_member_to_team_leader | Team Leader Choi | formal-polite | Greets Choi after returning from vacation. |
| 임꺽정 | 김 집사 | older_guild_member_to_guild_master | Kim hyung, then Guild Master | casual-but-respectful and self-correcting | Initially uses the familiar hyung address before correcting himself to Butler Kim's nominal Guild Master title. |
| 진태경 | 원명훈 | younger_brother_to_older_friend | hyung | casual-but-junior | Taekyung asks Won to speak casually and adopts hyung after they establish a friendly younger-brother relationship. |
| 원명훈 | 진태경 | older_friend_to_younger_brother | Taekyung | casual-affectionate | Won calls Taekyung 태경아 and welcomes him as a good younger brother. |
| 부천 헌터 협회장 | 진태경 | Hunter_Association_president_to_new_A-rank_Hunter | Mr. Jin Taekyung | formal-polite | Addresses Taekyung during the live A-Rank Hunter certification ceremony. |
| 최 팀장 | 원명훈 | Guild team leader to visiting Guild CEO | Mr. Won Myunghoon | formal-polite and probing | Choi questions Won about his eight-year absence and recruitment offer. |
| 원명훈 | 최 팀장 | visiting Guild CEO to Peace Guild team leader | Team Leader | formal-polite and deferential | Won asks Choi for permission to conduct a joint raid. |
| 원명훈 | 1팀장 | Star Guild CEO to Team 1 Leader | Team Leader 1; Jonghun | blunt-commanding | Won first uses the subordinate’s title, then switches to his personal name while ordering him to stay alert. |
| 1팀장 | 원명훈 | Star Guild Team 1 Leader to CEO | CEO | formal-deferential | Repeatedly addresses Won as 대표님 during the phone call. |
| 1팀장 | 진태경 | Star Guild Team 1 Leader to visiting Hunter | Hunter Jin Taekyung | formal-polite and flattering | Uses 진태경 헌터님 while praising Won Myunghoon's Aura. |
| 원명훈 | 김종훈 | Guild CEO to longtime subordinate | Jonghun | familiar and threatening | Uses Jonghun's personal name while rebuking him and warning him to stay focused. |
| 최 팀장 | 진태경 | guild_team_leader_to_guild_member | Mr. Jin Taekyung | formal-polite | Uses the full-name form 진태경 씨 while calling Taekyung during the emergency. |
| 홍천수 | 진태경 | older_comrade_to_younger_comrade | Taekyung | affectionate-casual | His remembered final words address Taekyung familiarly while ordering him to go ahead. |
| 진태경 | 홍천수 | younger_comrade_to_older_comrade | Cheonsu hyung | casual-but-junior | Taekyung called Hong Cheonsu hyung after being saved from goblins. |
| 카루스 | 진태경 | hostile monster to human enemy | human | halting and hostile | Carus addresses Taekyung as the human who took his eye. |
| 진태경 | 카루스 | hostile_enemy | Wyvern | hostile-casual | Taekyung addresses Carus as Wyvern while taunting him during their final battle. |
| 진태경 | 담당 검사 | interview_subject_to_prosecutor | Prosecutor | polite | Taekyung uses 검사님 while discussing the investigation. |
| 담당 검사 | 진태경 | prosecutor_to_investigated_Hunter | Mr. Jin Taekyung | formal-polite | The prosecutor uses 진태경 씨 while discussing the self-defense issue and thanking Taekyung. |
| 하연 | 김정희 | daughter_to_mother | Mom | casual-familiar | Hayeon calls 엄마 while reporting that Taekyung hit her. |
| 무명 | 거한 | monk_to_attacking_dark_path_officer | Benefactor | deferential but frightened | Uses 시주 while pleading with the officer and insisting that he started the attack. |
| 무명 | 진태경 | newly_met_monk_to_benefactor | Benefactor | formal-polite | Uses 시주 while asking Taekyung's name. |
| 무명 | 적천강 | junior_monk_to_legendary_martial_master | Great Hero Jeok Cheongang | formal-deferential | Identifies Jeok by the title Fire King and the honorific 대협. |
| 무명 | 굉도 | disciple_to_master | Master | deferential | Refers to Hong Dao as 스승님 while explaining his Dharma name and training. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 무명 | master_to_disciple | Disciple | affectionate and familiar | Hong Dao addresses Unnamed as 제자야 while discussing his residence. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 호위 | 남궁룡 | guard_to_family_head | Family Head | formal-deferential | The guards kneel and greet Namgung Ryong after he exits the pavilion. |
| 홍가 | 적천강 | frightened_stranger_to_overwhelming_martial_master | Mountain Spirit | fearful and pleading | The herbalist mistakes Jeok Cheongang for a mountain spirit and repeatedly begs for help. |
| 남궁룡 | 적천강 | family_head_to_legendary_martial_master | Fire King | formal-deferential | Namgung Ryong accepts three hundred silver nyang as compensation for offending Jeok Cheongang. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 젊은 호위 | 진태경 | family_guard_to_visiting_young_hero | Young Hero | formal but firm | The young guard questions Taekyung's iron balls and orders him to disarm. |
| 남궁룡 | 진태경 | Family Head to younger visiting martial artist | you | formal-but-familiar | Namgung Ryong uses 자네 while asking Taekyung to stop the duel. |
| 진태경 | 남궁룡 | younger visiting martial artist to Family Head | Family Head | formal-polite | Taekyung addresses Namgung Ryong as 가주님 while acknowledging his inability to stop his father. |
| 진태경 | 남궁천 | junior martial artist to legendary martial master | Great Hero Nangong Cheon | formal-deferential | Taekyung uses the title and honorific 대협 when formally greeting the Azure Sky Sword King. |
| 남궁천 | 진태경 | legendary martial master to audacious junior | you / brat | blunt and intimidating | Namgung Cheon uses 네 녀석 and 놈 while testing and threatening Taekyung. |
| 남궁옥 | 진태경 | hostile young family heir to visiting martial artist | you bastard | hostile and enraged | Nangong Ok confronts Taekyung after overhearing the conversation with his father. |
| 진태경 | 남궁옥 | older martial artist to hostile young family heir | young friend | mock-polite and patronizing | Taekyung calls Nangong Ok 젊은 친구 after stopping his sword draw. |
| 남궁천 | 남궁룡 | father_to_son | you | formal-but-familiar | Nangong Cheon speaks to his sixty-year-old son while discussing martial mastery and Taekyung. |
| 수하 | 흑종필 | subordinate_to_bandit_leader | Boss | deferential | A Black Mountain Stronghold subordinate reports the Green Forest Alliance’s letter and the merchant route. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 점소이 | 상인 | waiter_to_customers | gentlemen | formal-polite | The waiter addresses the merchants as 손님들 while charging them for their supposed friend's bill. |
| 점소이 | 송호 | waiter_to_respected_martial_master | Great Hero Song | formal-deferential | The waiter recognizes Song Ho and bows before accepting payment. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 아이들 | 청년 | children_to_stranger | beggar bastard | childlike-insulting | The children repeat their mother's insulting description of Taekyung's beggar-like appearance. |
| 종리추 | 진태경 | new acquaintances | friend; you | casual and overly familiar | Jongni Chu immediately declares Taekyung his friend and persistently follows him. |
| 진태경 | 종리추 | new acquaintances | you; Jongni Chu; punk | blunt and dismissive | Taekyung rejects Jongni Chu's forced friendship and repeatedly tells him to leave. |
| 포목점 종업원 | 진태경 | shop employee to customer | beggar | condescending and hostile | The employee assumes Taekyung entered the cloth shop to beg and insults him over his clothing and money. |
| 위팽 | 혁무진 | mentor_to_junior_martial_artist | Hyuk Mujin | blunt and testing | Wipeng addresses Mujin by name when beginning to assess and train him. |
| 혁무진 | 위팽 | junior_martial_artist_to_mentor | Great Hero Wipeng | formal-deferential | Mujin uses 위팽 대협 when reacting to Wipeng's recognition and instruction. |
| 호철 | 혁무진 | squad_subordinate_to_vice_squad_leader | Vice Squad Leader | deferential | Hocheol addresses Mujin by his Jin Dragon Squad office. |
| 적천강 | 남궁룡 | legendary_martial_master_to_family_head | Family Head Nangong | familiar and teasing | Jeok calls him 남궁 가주 while asking whether his son will compete. |
| 적천강 | 공일중 | senior_martial_master_to_sect_leader | you; man with the sycophant's beard | blunt and insulting | Jeok mocks Gong's beard and dismisses the title Wind-and-Cloud Sword Lord. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 대머리 사내 | 곽철융 | bookmaker_to_respected_gambler | Great Hero Kwak | formal-deferential | The bald bookmaker respectfully addresses Kwak Cheolyung while acknowledging his status as a legendary Dogon. |
| 감독관 | 진태경 | exam_supervisor_to_candidate | Young Hero Jin | formal-polite | Uses 진 소협 while calling Taekyung for the cliff test. |
| 진태경 | 감독관 | candidate_to_exam_supervisor | Supervisor | polite | Uses 감독관님 while asking about the test conditions and result. |
| 감독관 | 철수신룡 | exam_supervisor_to_overpowering_candidate | you | formal-commanding | Orders the Iron-Water Divine Dragon to control himself and warns him against fighting. |
| 철수신룡 | 감독관 | overpowering_candidate_to_exam_supervisor | you | blunt-commanding | Orders the supervisor to move aside while asserting his status as Pa Ryun's disciple. |
| 진태경 | 철수신룡 | rival_candidates | you; weakling | insulting-casual | Uses 너 and later insults him as 좆밥아 while provoking him. |
| 철수신룡 | 진태경 | rival_candidates | brat; you | condescending and taunting | Uses 애송아 and 네놈 while belittling Taekyung and the Fire Gate Clan. |
| 백우 | 진태경 | rival_finalists | Fellow Daoist Jin Taekyung | formal-polite and admonishing | Baek Woo uses 도우 while criticizing Taekyung's vulgarity. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 백우 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Baek Woo, Gung Gibang, and Zhuge Gyun collectively as 세 얼간이. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 제갈균 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Zhuge Gyun as part of the trio and threatens them before a duel. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 중년 감독관 | 송호 | exam_supervisor_to_respected_Peak_master | Sir Song | formal-deferential | Uses 송 대협 while respectfully asking why Song Ho has come. |
| 종리추 | 청풍 | newly met fellow finalist | friend | casual and overly familiar | Jongni Chu immediately calls the disguised Cheongpung friend after learning his false identity. |
| 청풍 | 종리추 | newly met fellow martial artist | friend | casual and exuberant | Cheongpung enthusiastically accepts Jongni Chu's offer of friendship while still using his disguise. |
| 굉도 | 팽 시주 | senior_martial_master_to_rival_martial_master | Benefactor Peng | formal-polite | Hong Dao uses the Buddhist 시주 address while asking Peng Cheolhu to explain Jongni Chu's hidden strength. |
| 심사관 | 진태경 | judge_to_finalist | Young Hero Jin | formal-polite and flustered | Warns Taekyung that entering the semifinal violates the banquet rules. |
| 진태경 | 심사관 | finalist_to_judge | Judge | blunt and defiant | Rejects the judge's demand that he stand by while Cheongpung is apparently endangered. |
| 적천강 | 심사관 | presiding_chair_to_judge | you | commanding and intimidating | Orders the judge to abandon the original schedule and begin the final. |
| 적천강 | 종리추 | legendary_master_to_suspicious_rival | you / tongue-cut bastard | grave and threatening | Questions Jongni Chu about Tianshan and threatens him over harm to Taekyung or Cheongpung. |
| 종리추 | 적천강 | suspicious_rival_to_legendary_master | you | polite and taunting | Refuses to answer Jeok Cheongang directly and hints at the danger to his Disciple. |
| 개방의 제자들 | 적천강 | Beggars' Sect disciples to legendary martial master | Great Hero Jeok | formal-deferential | They bow and report that their Sect Leader is pursuing Jongni Chu. |
| 개방의 제자들 | 굉도 | Beggars' Sect disciples to injured Buddhist master | Master | formal-urgent | They urgently plead with Hong Dao to come to his senses after finding him gravely wounded. |
| 염호 | 한수 | old friends | Han Su; you bastard | rough and familiar | Flame Tiger insults Han Su while criticizing his treatment of the captured agent. |
| 한수 | 염호 | old friends | Flame Tiger | familiar and conversational | Han Su addresses his longtime friend by his epithet while agreeing to proceed together. |
| 한수 | 무명 | hostile_intruder_to_Shaolin_monk | Hong Dao's Disciple; you | cold and threatening | Han Su identifies Unnamed as Hong Dao's Disciple and threatens to take his life. |
| 무명 | 한수 | Shaolin_monk_to_hostile_intruder | Benefactor | formal-polite but guarded | Unnamed uses 시주 while refusing Han Su's demand for the Green Jade Buddha Staff. |
| 염호 | 굉천 | hostile_martial_opponents | Brat; bald monk | condescending and taunting | Flame Tiger repeatedly belittles Hongcheon during their battle. |
| 굉천 | 염호 | hostile_martial_opponents | old monster; demonic fiend | defiant and condemning | Hongcheon condemns Flame Tiger as an old monster and demonic fiend while continuing to resist. |
| 염호 | 적천강 | hostile martial opponents | old man; Fire King | hostile and taunting | Flame Tiger taunts Jeok while using Hongcheon as a hostage and later recognizes him as the Fire King. |
| 적천강 | 염호 | rival martial opponents | Flame Tiger; bear | blunt, threatening, and contemptuous | Jeok dismisses Flame Tiger's attempt to imitate a fox and calls him a foolish bear before killing him. |
| 진태경 | 염호 | hostile martial opponents | yellow old geezer | insulting and casual | Taekyung exchanges color-based insults with Flame Tiger during their joint attack. |
| 염호 | 진태경 | hostile martial opponents | green little brat | hostile and condescending | Flame Tiger insults Taekyung while attempting to kill him first. |
| 한수 | 혈주 | operative to rendezvous contact | Blood Lord | relieved and deferential | Han Su calls out to the Blood Lord after escaping Jeok Cheongang. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 한수 | rendezvous_contact_to_senior_operative | Senior Yin Ghost | mock-polite and lightly taunting | Uses 음귀 선배님 while teasing Han Su for hesitating to make his request. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 혈주 | 종리추 | hostile_opponents | you; fearless bastard | hostile and suspicious | The Blood Lord questions Jongni Chu's identity and calls him the fearless man who interfered with his attack on Hong Dao. |
| 종리추 | 혈주 | opponents | you | calm and admonishing | Jongni Chu addresses the Blood Lord as 자네 while explaining that he must stop him by force. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 종리추 | 송호 | old_acquaintances; former_savior_and_survivor | Thousand-Faced Fox Song Ho; you | casual-familiar | Mae Jonghak addresses Song Ho informally, asks about his prosthetic leg, and recalls that Song would be the first to recognize him. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 진태경 | 진하연 | older_brother_to_younger_sister | Jin Hayeon | blunt-familiar; deliberately stern | Taekyung uses Hayeon's full name to make her hesitate while defending his implausible explanation for sleeping forty-two hours. |
| 최 팀장 | 송송이 | guild_team_leader_to_guild_member | Miss Song | formal-polite | Directs Song Song to take charge of post-raid cleanup and perimeter security. |
| 박지훈 | 진태경 | former_middle_school_classmates | Taekyung | casual-familiar and teasing | Uses 태경아 and 너 while reconnecting after eleven years. |
| 진태경 | 박지훈 | former_middle_school_classmates | you | casual-familiar and teasing | Uses 너 while joking about Jihoon's wealth, appearance, and school memories. |
| 박지훈 | 1팀장 | de_facto_superior_to_nominal_team_leader | Team Leader | commanding and condescending | Orders the nominal Team 1 Leader to wait, arrange an A-Rank raid, and stop imitating a superior. |
| 1팀장 | 박지훈 | nominal_team_leader_to_de_facto_superior | Mr. Jihoon | formal-deferential and anxious | Uses 지훈 씨 while cautiously reporting on Team Leader Jung Hyunwoo and obeying Jihoon's instructions. |
| 김진수 | 진태경 | rookie_guild_member_to_senior_Hunter | Senior | formal-deferential | Jinsoo addresses Taekyung as 선배님 while introducing himself and asking permission to speak comfortably. |
| 진태경 | 김진수 | senior_Hunter_to_rookie_guild_member | Jinsoo | formal-polite | Taekyung uses 진수 씨 after praising Jinsoo’s performance. |
| 임영준 | 진태경 | hostile_black_hunter_to_target | Jin Taekyung; kid | hostile and condescending | Recognizes Taekyung and taunts him as an overconfident child before ordering the attack. |
| 진태경 | 임영준 | target_to_black_hunter_attacker | you | insulting and casual | Demands that Im Yeongjun surrender with the other two attackers and mocks his lack of judgment. |
| 블랙 헌터 | 임영준 | subordinate_to_team_leader | Team Leader | formal-urgent | A surviving Black Hunter cries out to Im Yeongjun after Taekyung destroys his shoulder. |
| 박지훈 | 박태섭 | Myeongdong Guild subordinate to Guild Master; junior to senior | Guild Master; great senior | formal but sarcastic | Uses 길드장님 and 대선배님 while openly challenging Park Tae Seop's authority. |
| 박태섭 | 박지훈 | Guild Master to subordinate; senior to junior | you; brat | furious and condescending | Uses hostile forms while confronting Jihoon over Jung Hyunwoo's death and the Black Hunter problem. |
| 진태경 | 김철수 | visiting Hunter to Security Team Hunter | Hunter Kim Cheol Soo | polite and manipulative | Taekyung addresses him formally while promising to mention his loyalty to the Guild Master. |
| 김철수 | 진태경 | Security Team Hunter to visiting Hunter | Hunter Jin Taekyung | formal-polite and admiring | Initially uses 선생님, then recognizes Taekyung and addresses him as 진태경 헌터님. |
| 진태경 | 선배님들 | junior_to_senior_team_members | Seniors | polite-but-threatening | Taekyung addresses the Myeongdong Guild Team 1 Hunters while ordering them to clear a path. |
| 최민우 | 박지훈 | rival Guild Team Leader to hostile Guild Hunter | Hunter Park Jihoon | formal-polite and controlled | Calls Jihoon through Manager Kim’s phone after the Peace Guild captures Myeongdong personnel. |
| 진태경 | 박태섭 | visiting Hunter to Guild Master | Guild Master | polite but sarcastic | Uses 길드장님 while asking whether Jihoon is Tae Seop's son and warning him not to interfere. |
| 박태섭 | 진태경 | Guild Master to hostile visiting Hunter | you | formal-but-familiar and cautioning | Uses 자네 while warning Taekyung about the danger of opposing 'that person' before reluctantly fighting him. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 박태섭 | 이정룡 | Guild Master to Vice Guild Master; former Great Cataclysm acquaintance | Vice Guild Master Lee Jungryong | formal-deferential | Park Tae Seop greets Lee respectfully while apologizing for the scene. |
| 이정룡 | 박태섭 | Vice Guild Master to Guild Master; former Great Cataclysm acquaintance | Guild Master Park | formal-but-familiar | Lee minimizes their relationship as occasional acquaintances while presenting himself as conciliatory. |
| 박지훈 | 이정룡 | Disciple to master | Master | terrified and pleading | Jihoon cries out to Lee as Master after Taekyung begins stabbing him. |
| 이정룡 | 박지훈 | master to Disciple | Disciple | commanding, protective, and enraged | Lee restrains himself to protect Jihoon while ordering Taekyung to stop and later carries Jihoon's mutilated body. |
| 이정룡 | 석 팀장 | Vice Guild Master to security-team leader | Team Leader Seok | formal-but-familiar and commanding | Lee addresses Seok while assuring Park Tae Seop that the Myeongdong Guild members will be safe and later orders him to watch Taekyung. |
| 석 팀장 | 이정룡 | security-team leader to Vice Guild Master | Vice Guild Master | formal-deferential | Seok reports on Park Tae Seop and the operation, then accepts Lee's orders. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 임꺽정 | 최 팀장 | guild_member_to_team_leader | Team Leader Choi | hearty and grateful | Thanks Choi for paying for and arranging his treatment. |
| 최 팀장 | 이정룡 | former_subordinate_to_former_superior; junior_to_senior | Vice Guild Master; Senior | formal but hostile and controlled | Uses the official title in greeting Lee and 선배님 while confronting him about the overseas transfer and their shared past. |
| 김 집사 | 이정룡 | former_savior_to_saved_senior; hostile acquaintances | Senior | formal-polite turning openly threatening | Uses 선배 while greeting Lee and later threatens him after recalling the Mapo Bridge rescue. |
| 이정룡 | 김 집사 | older_acquaintance_to_former_savior | Hwajong; you | familiar, needling, and amused | Calls Butler Kim 화종이 and 자네 while provoking him about his temper and the rescue. |
| 김 집사 | 석고준 | senior_Hunter_to_junior_security_leader | Hunter; Team Leader Seok | blunt and contemptuous | Initially addresses Go Jun as 헌터님, then dismisses him as 석고준 팀장 and orders him to stay out of the conversation. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter Jin Taekyung | formal-deferential | Uses Taekyung's full Hunter title while asking how he possesses the Mana Cultivation Method. |
| 김 집사 | 송송이 | guild_master_to_guild_member | Hunter Song Song | formal-deferential | Uses Song Song's full Hunter title while checking on her after the retching. |
| 댕댕이 | 진태경 | new_hire_to_senior_Hunter | Senior Jin Taekyung | fearful-deferential | A first-day trainee begs Taekyung to let him leave the A-rank Gate. |
| 진태경 | 스켈레톤 워로드 | hostile_monster_encounter | friend; Warlord | mocking-casual | Taekyung sarcastically calls the damaged Warlord his friend, then addresses it by its title while threatening to kill it. |
| 스켈레톤 워로드 | 진태경 | undead_ruler_to_human_enemy | Human | halting-hostile, then desperate-deferential | The Warlord addresses Taekyung as 인간이여 while trying to recruit or dominate him, then shifts into polite pleading when threatened. |
| 서울지부 협회장 | 최민우 | Hunter Association official to Peace Guild Master | you | authoritative and patronizing | Uses 자네 while delaying the Peace Guild's entry and ordering them to follow procedure. |
| 최민우 | 서울 중앙 협회장 | Peace Guild Master to Hunter Association official | Association President | formal but defiant | Choi openly treats his declaration that the Peace Guild will lead as a notification rather than a request. |
| 서울 중앙 협회장 | 최민우 | Hunter Association official to Peace Guild Master | you | authoritative and patronizing | Uses 자네 while objecting to Choi's defiance and later dismissing the Guild's responsibility. |
| 석고준 | 서울 중앙 협회장 | Ares security leader to Hunter Association official | Association President | formal-polite and coercive | Encourages the Association President to let the Peace Guild lead while applying indirect pressure. |
| 서울 중앙 협회장 | 석고준 | Hunter Association official to Ares security leader | Team Leader Seok | formal-polite and deferential | Asks Go Jun to put in a good word with Lee Jungryong and accepts his framing of the operation. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 진태경 | 이우중 | Hunter to Association President | President Lee Woojoong | mock-polite and confrontational | Taekyung addresses him as 이우중 협회장님 while condemning his conduct during the delayed rescue. |
| 이우중 | 진태경 | Association President to Hunter | Jin Taekyung; young man | authoritative and indignant | Woojoong addresses Taekyung with 젊은 친구 and 진태경 당신 while objecting to his insults. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 현장 리포터 | 진태경 | field_reporter_to_returned_Hunter | Mr. Jin Taekyung | formal and startled | The reporter urgently confirms Taekyung's identity during the live broadcast. |
| 진태경 | 워로드몬 | captor_to_captured_monster | Warlordmon | mocking-commanding | Taekyung uses the childish nickname while ordering the Skeleton Warlord to perform tricks. |
| 여성 | 빙빙 | mother_to_daughter | Bingbing | urgent-familiar | The mother urgently tells Bingbing to hold her hand while they flee the Monster Wave. |
| 이정룡 | 백한성 | Ares authority to national head of state | Mr. President | formal-polite | Uses 대통령 각하 while greeting Baek Hanseong. |
| 백한성 | 이정룡 | President to Ares Guild Vice Guild Master | Vice Guild Master Lee | formal-polite | Uses 이정룡 부길드장님 while discussing the Chinese proposal. |
| 낙양괴의 | 매종학 | physician_to_renowned_martial_master | Great Hero Mae | formal-polite | Addresses Mae while asking him to protect Taekyung and while requesting that he calm down. |
| 매종학 | 낙양괴의 | renowned_martial_master_to_physician | Strange Physician | familiar-but-respectful | Uses 괴의 while checking on the physician and calming him. |
| 진태경 | 낙양괴의 | young_martial_artist_to_physician | Elder; Strange Physician | deferential and urgent | Uses 어르신 and 괴의 while asking for Jeok Cheongang's diagnosis and treatment. |
| 낙양괴의 | 진태경 | senior_physician_to_young_martial_artist | young brat | gruff and murderous | Threatens Taekyung's eyes and mouth while maintaining a deceptively genial demeanor. |
| 주화란 | 허준 | niece_to_uncle | Uncle Heo | formal-polite | Hwaran addresses her uncle and Chief Escort as 허 숙부. |
| 허준 | 주화란 | uncle_to_niece | Hwaran; Young Bureau Head | concerned-familiar and commanding | Heo Jun calls her 화란아 and orders the escorts to protect the Young Bureau Head. |
| 천력부 | 허준 | familiar_enemies | Brother Heo | taunting and insulting | Heavenly Axe recognizes Heo Jun and mocks his service to Hwaran. |
| 허준 | 천력부 | escort_chief_to_mounted_bandit_leader | Heavenly Axe | alarmed and guarded | Heo Jun identifies the approaching bandit leader by his epithet. |
| 천력부 | 주화란 | mounted_bandit_leader_to_young_bureau_head | little girl | condescending and insulting | Heavenly Axe refers to Hwaran contemptuously while mocking Heo Jun. |
| 주화란 | 석 표두 | childhood_siblings_by_affection | Brother Seok; Chief Escort Seok | grieving and respectful | Hwaran calls him Brother Seok before correcting herself to his office title while mourning his death. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 천력부 | superior_martial_artist_to_defeated_bandit_leader | Axe; our Axe | mocking-casual | Taekyung deliberately shortens Heavenly Axe's epithet to 력부야 and 우리 력부 while preventing his retreat. |
| 천력부 | 진태경 | bandit_leader_to_overwhelming_younger_martial_artist | Sleeping Dragon of Shanxi; Young Hero Jin; young punk | shifting from startled-deferential to condescending | Bangyeol recognizes Taekyung by his epithet and formal title, then becomes contemptuous after believing Jeok Cheongang is absent. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 호위장 | 백무성 | Xi'an Tower head guard to visiting Huashan master | Great Hero Baek | formal-deferential | Praises Baek's reputation and defers to him when Hyuk Sopyung arrives. |
| 백무성 | 혁소평 | fellow young sect prodigies and prior acquaintances | you | familiar and composed | Greets Hyuk as an old acquaintance before the confrontation. |
| 혁소평 | 백무성 | fellow young sect prodigies and prior acquaintances | you | hostile and confrontational | Uses 당신 while angrily questioning why Baek is at Xi'an Tower. |
| 혁소평 | 진태경 | hostile_opponents | you; bastard | hostile and contemptuous | Hyuk insults Taekyung as a beggar and attacks him after Taekyung refuses to defer to his status. |
| 진태경 | 혁소평 | hostile_opponents | you; bastard | insulting and taunting | Taekyung mocks Hyuk’s appearance, cultivation, and failed attack while forcing him to agree to end the dispute. |
| 혁소평 | 송 총관 | visitor_to_establishment_manager | Manager Song | condescending and threatening | Uses 우리 송 총관 while belittling Xi’an Tower’s chief manager. |
| 서안루 총관 | 혁소평 | establishment_manager_to_visiting_martial_artist | Young Hero Hyuk | formal-polite and firm | Warns Hyuk Sopyung that Xi’an Tower will formally complain to the Zhongnan Sect. |
| 봉수 | 혁소평 | junior_disciple_to_same_generation_senior_disciple | Senior Brother | urgent and deferential | Uses 대사형 while urgently summoning Hyuk Sopyung. |
| 혁소평 | 봉수 | same_generation_disciple_to_junior_disciple | Junior Brother | familiar and commanding | Recognizes Bong-su as a Junior Brother despite their different Masters. |
| 혁소평 | 황보엄 | junior_disciple_to_senior_martial_uncle | Senior Martial Uncle | formal-deferential but strained | Hyuk Sopyung repeatedly addresses Hwangbo Eom as 사백 while resisting his criticism. |
| 황보엄 | 혁소평 | senior_martial_uncle_to_junior_martial_artist | you; nobody like you | cold and contemptuous | Hwangbo Eom uses 네 녀석 and 네까짓 놈 while reprimanding Hyuk Sopyung. |
| 주화란 | 황보엄 | visitor_to_Zhongnan_senior_martial_uncle | Great Hero Hwangbo | formal-deferential | Ju Hwaran formally introduces herself to Hwangbo Eom as the Taeeul Merciless Sword. |
| 황보엄 | 주화란 | Zhongnan senior to Yongbong Young Bureau Head | you | cold, commanding, and manipulative | Uses 자네 while ordering Hwaran to open the casket and demanding compensation. |
| 진태경 | 황보엄 | junior_martial_artist_to_Zhongnan_senior | Great Hero Hwangbo | casual-polite and teasing | Taekyung uses 황보 대협 after deliberately pretending not to recognize Hwangbo. |
| 백무성 | 황보엄 | junior_martial_artist_to_Zhongnan_senior | Great Hero Hwangbo | formal-deferential | Baek introduces himself with 황보 대협. |
| 황보엄 | 진태경 | Zhongnan_senior_to_younger_martial_artist | insolent brat | blunt, amused, and probing | Hwangbo describes Taekyung as a 건방진 아해 and later treats him as a youngster. |
| 궁기방 | 흑걸개 | childhood_friends | Big Nose | familiar and teasing | Gung Gibang uses 왕코 for Heukgeol, whom he has known since their youth as beggars. |
| 흑걸개 | 궁기방 | childhood_friends | Gibang; Successor Beggar | rough and familiar | Heukgeol alternates between 기방이 and the title 후개 while scolding his old friend. |
| 월화 | 황보엄 | Lower_District_Sect_leader_to_Zhongnan_senior | Great Hero Hwangbo | formal-polite and firm | Wolhwa respectfully addresses Hwangbo while refusing to withdraw from the commission. |
| 황보엄 | 월화 | Zhongnan_senior_to_Lower_District_Sect_leader | you | cold and commanding | Hwangbo orders Wolhwa to withdraw from the dispute. |
| 궁기방 | 황보엄 | Beggars_Sect_successor_to_Zhongnan_senior | Great Hero Hwangbo | formally deferential but defiant | Gung invokes Hwangbo's title while asserting the Beggars' Sect's pride and rules. |
| 흑걸개 | 황보엄 | Beggars_Sect_branch_leader_to_Zhongnan_senior | Great Hero Hwangbo | deferential and evasive | Heukgeol uses the respectful title while refusing to withdraw the branch's support. |
| 황보엄 | 적천강 | rival_martial_masters | Fire King Jeok Cheongang | cold and taunting | Reveals that he knows Jeok's illness and threatens to settle his bad blood with the Fire Gate Clan. |
| 황천 | 황보엄 | junior_disciple_to_senior_martial_uncle | Senior Martial Uncle | urgent and deferential | Uses 사백님 while demanding that Taekyung release Hwangbo Eom. |
| 황천 | 진태경 | sect_disciple_to_hostile_younger_martial_artist | you bastard | hostile and commanding | Orders Taekyung to release Hwangbo Eom. |
| 황천 | 혁소평 | junior_disciple_to_senior_disciple | Senior Brother | deferential and alarmed | Appeals to Hyuk Sopyung after he orders the unit to withdraw. |
| 혁소평 | 황천 | senior_disciple_to_junior_disciple | Junior Brother | gentle but commanding | Orders Hwangcheon to withdraw and then silences his objection. |
| 혁소평 | 주화란 | senior_Zhongnan_disciple_to_young_bureau_head | Young Lady Ju | formal-apologetic | Hyuk apologizes on Zhongnan's behalf; Ju Hwaran rejects the address and orders him to call her Young Bureau Head. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 송일섬 | 궁기방 | senior_martial_artist_to_Beggars_Sect_successor | Successor Beggar | blunt and irritated | Uses 후개 while objecting to Gung Gibang’s spitting and insults. |
| 궁기방 | 송일섬 | Beggars_Sect_successor_to_young_escort_captain | Young Hero Song | casual and admiring | Uses 송 소협 while praising the famous Soul-Chasing Guest and comparing their looks. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 무송 | 황태구 | captor_to_defeated_bandit | you | hostile-commanding | Mu Song orders Hwang Tae-gu to accept the League's punishment after destroying his martial arts. |
| 황태구 | 무송 | defeated_bandit_to_captor | you bastard | hostile-defiant | Hwang Tae-gu threatens Mu Song and the Water Dragon Stronghold bandits before losing consciousness. |
| 무송 | 관리 | river-bandit leader to military official | General | casual-familiar | Uses 장군 while requesting permission to put passengers ashore. |
| 관리 | 무송 | military official to Stronghold Lord | Stronghold Lord | formal-polite | Uses 채주 while wishing Mu Song martial fortune. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 진태경 | 당사독 | visitor_to_Sichuan_Tang_Family_Head | Great Hero Tang Sadok | formal-deferential | Taekyung formally introduces himself and addresses Tang Sadok as 대협. |
| 당사독 | 진태경 | Family_Head_to_visiting_younger_martial_artist | you; fearless brat | blunt and threatening | Tang Sadok uses 너 and later calls Taekyung 겁 없는 놈 while rejecting his challenge. |
| 청풍 | 당사독 | young_martial_artist_to_Sichuan_Tang_Family_Head | Family Head | formal-deferential | Cheongpung addresses Tang Sadok as 가주님 while appealing for help. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 청성파의 장로들 | 진태경 | Qingcheng_Sect_Elders_to_Young_Hero | Young Hero Jin | formal-deferential | The Elders announce that the Sect Leader has ordered them to help Jin find the Divine Physician. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 사천성주 | 애향이 | lord_to_favorite_concubine | Aehyang | affectionate-familiar | The City Lord uses her personal name while discussing the visitors. |
| 애향이 | 사천성주 | favorite_concubine_to_city_lord | My lord | seductive-deferential | Aehyang repeatedly addresses the City Lord as 대인 while persuading him to receive Taekyung. |
| 청성파의 두 장로 | 묘령사태 | allied_sect_elders_to_injured_nun | Venerable Myoryeong | formal and urgent | They call out to Myoryeong after hearing that the Heaven-Shaking Venerable Nun has died. |
| 묘령사태 | 진태경 | injured_allied_nun_to_young_hero | Young Hero Jin | formal-deferential | Uses 진 소협 after recognizing that Taekyung already understands the likely connection between the attacks. |
| 진태경 | 동봉 | visitor_to_divine_physician | Old Man Dong | formal-polite and deferential | Adopts Dong Feng's requested address after learning his personal name. |
| 청풍 | 동봉 | newly_met_young_martial_artist_to_older_friend | Old Man Dong | casual and cheerful | Accepts Dong Feng's invitation to regard him as an older friend. |
| 문경 | 동봉 | disciple_to_master | Master | deferential and apologetic | Reveals Dong Feng's identity and apologizes for bringing the party without permission. |
| 동봉 | 진태경 | physician_to_visiting_young_martial_artist | Young Master Jin | formal-polite and gentle | Uses 진 공자 while welcoming and speaking with Taekyung. |
| 동봉 | 문경 | master_to_disciple | Gyeong | familiar-commanding | Dong Feng tells Mungyeong to remain at the clinic and care for the patients. |
| 당사독 | 동봉 | Tang Family Head to visiting physician | you | blunt and testing | Uses 그대 while demanding Dong Feng's identity and purpose. |
| 당사독 | 문경 | Family Head to visiting medical apprentice | you | blunt and probing | Asks whether Mungyeong is the Divine Physician's Disciple. |
| 동봉 | 당사독 | physician to Family Head | you | formal-polite and measured | Uses 그대 while explaining that Tang Sadok must know Tang Mimi is unusual. |
| 당사독 | 궁 노인 | Family Head to prison caretaker | Old Man Gung | familiar-supervisory | Tang Sadok asks about the prisoners and addresses the caretaker by surname and elder form. |
| 궁 노인 | 당사독 | prison caretaker to Family Head | Family Head | deferential | Uses 가주님 while greeting Tang Sadok and reporting on the prisoners. |
| 서천마군 | 기련삼괴 | commander_to_subordinates | Three Fiends; Three Old Men | mocking and superior | Calls them 삼괴 and then mockingly says they may now be called 삼노. |
| 기련삼괴 | 서천마군 | subordinates_to_commander | my lord | fearful and deferential | The brothers greet the Western Heaven Demon Lord as 마군. |
| 진태경 | 천력마 | prisoner_feeder_to_prisoner | you | casual and mocking | Taekyung questions the Heavenly Power Demon and mocks him as the Kunlun Sect's public-pissing criminal. |
| 천력마 | 진태경 | prisoner_to_prisoner_feeder | you | gruff and self-possessed | The Heavenly Power Demon speaks of himself as 노부 while questioning Taekyung. |
| 수문각주 | 당사독 | nephew_to_uncle | Uncle | urgent-deferential | Uses 숙부님 when urgently entering and reporting to Tang Sadok. |
| 호위 | 당사독 | guard_to_Family_Head | Family Head | formal-deferential | Uses 가주님 while reporting Jin Taekyung's request. |
| 당사독 | 수문각주 | uncle_to_nephew | you; pathetic fool | blunt-rebuking | Tang Sadok uses 네 녀석 and 한심한 놈 while correcting his nephew's underestimation of the enemy. |
| 당사독 | 녹영대원 | Family Head to subordinate | you | formal-commanding | Tang Sadok uses 자네 while questioning the injured Green Shadow Squad martial artist. |
| 서천마군 | 당사독 | hostile_opponents | you | calm and taunting | The Western Heaven Demon Lord uses 자네 while answering Tang Sadok's question. |
| 당사독 | 서천마군 | hostile_opponents | you bastard | hostile and threatening | Tang Sadok uses 네놈 after recognizing the disguised infiltrator. |
| 일괴 | 당진후 | enemy_to_enemy; former_acquaintances | youngster | mocking and taunting | First Fiend recognizes Tang Jinhu and repeatedly addresses him as a youngster while threatening the Tang Clan. |
| 당진후 | 일괴 | enemy_to_enemy | you; Fiend | hostile and defiant | Tang Jinhu calls First Fiend a Fiend and vows to kill him. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 당사독 | 청풍 | family_head_to_younger_ally | greenhorn | blunt and protective | Tells Cheongpung not to interfere while calling him a 핏덩이. |
| 서천마군 | 일괴 | commander_to_subordinate | First Fiend | commanding and cold | Orders First Fiend to handle Cheongpung and warns him that Cheongpung is dangerous. |
| 일괴 | 서천마군 | subordinate_to_commander | Demon Lord | deferential and fearful | Answers the Western Heaven Demon Lord's orders as 마군 and submits after being threatened. |
| 일괴 | 청풍 | enemy_to_assigned_target | greenhorn; brat | mocking and bloodthirsty | Calls Cheongpung the Sword Saint's successor and boasts that he will leave him barely breathing. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 동 노인 | benefactor_to_divine_physician | Old Man Dong | formal-polite and urgent | Taekyung uses 동 노인 while urging the injured Divine Physician to remain back. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 십왕     | **Ten Kings**       |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 극양                        | **Extreme Yang**      |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 흑룡갑 | **Black Dragon Armor** | Defensive armor worn beneath the Western Heaven Demon Lord's yellow robe. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 364
- **Aliases:** Medicine Immortal
- **Role:** Legendary physician also known as Dong Feng and Mungyeong's Master, who survived the Western Heaven Demon Lord's attack but lost his dantian and martial arts and suffered a broken wrist while shielding Jeok Cheongang.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is his Disciple; Dong Feng’s own Master was a martial artist and physician who left the Murim and became a doctor to erase his accumulated killing karma, and Dong Feng left the Luoyang Strange Physician a porcelain-shard token directing him to Sichuan.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 364
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** A legendary wandering martial master and Jin Taekyung's Master and intended heir, Jeok Cheongang is awake but weakened and remains engaged in a confrontation with the Western Heaven Demon Lord.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 364
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, who has reached the Supreme Peak realm through enlightenment and remains engaged in the confrontation with the Western Heaven Demon Lord.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 364
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 364
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and remains alive and hostile in the confrontation.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃365화



‘이런 느낌이었나.’

초절정. 하늘에게 선택받은 위대한 무인들의 영역.

나는 지금껏 허락되지 않았던 그곳을 향해 한 걸음을 내디뎠고, 끝없는 자유를 느꼈다.

지금 이 기분은 뭐랄까…….

‘끝내주네.’

어느새 입가에는 희미한 웃음이 맺혀 있었다.

띠링. 띠링. 띠링.



- [열화신공]의 경지가 팔 성으로 상승했습니다.

- [화룡신창]의 경지가 팔 성으로 상승했습니다!

- [염화일로]의 경지가……!



각종 무공의 상승, 그에 따른 레벨업과 업적 달성을 알리는 시스템 알림이 쉬지 않고 울려 퍼진다.

전신 깊숙한 곳에서 용암과도 같은 기운이 솟아올랐다. 나와 적천강을 향해 덮쳐 오는 어둠이 조금도 두렵지 않았다.

“죽어엇!”

비명과도 같은 외침. 악귀처럼 일그러진 얼굴.

사람 좋은 웃음을 입가에 머금고 있던 중년인의 모습은 이제 어디에서도 찾아볼 수 없다.

그저 살심(殺心)에 사로잡힌 괴물만이 있을 뿐이다.

슈와아아악!

광폭한 살기에 휩싸인 묵빛 검강이 낙뢰처럼 내리꽂혔다. 보는 것만으로도 그 안에 도사린 파괴적인 기운이 느껴진다.

하지만…….

‘결국, 너도 사람이었구나.’

지금의 서천마군은 부상과 피로로 이미 지쳤고, 필요 이상의 분노는 마음을 흩트려 놓았다.

마음이 흔들리면 기운도 흔들리는 법. 바늘로 바위를 뚫을 수는 없어도 모래 알갱이 사이를 통과하는 것은 어렵지 않다.

스윽.

단 한 걸음. 발끝이 지면을 밀자 공간이 사라졌다.

어느새 자신의 앞을 가로막은 내 뒷모습에, 적천강이 다급한 음성을 토해 냈다.

“이 녀석, 당장 물러…….”

적천강의 목소리는 이어지지 못했다. 백염의 투명한 창날 위로 솟구친 청백색의 기운 때문이었다.

극양(極陽)의 열기가 실린 그것은 실타래가 엉키듯 서로를 향해 이어지고, 뭉쳐졌으며 마침내 하나의 형태를 이루었다.

아름답고도 파괴적인 공력의 집합체. 위대한 무인들의 전유물.

‘강기(罡氣).’

드디어 여기까지 이루었다.

나는 환희로 몸을 떨며 덮쳐드는 어둠을 향해 팔을 내뻗었다.

쉬익-!

허공에 그어지는 한 줄기의 선. 화살처럼 쏘아진 청백색의 불꽃이 어둠과 맞닿는다.

천격(天格).

화룡의 발톱이 묵색 강기를 찢어발겼다.

콰아아아아!

귀가 먹먹해지는 굉음 사이, 똑똑히 볼 수 있었다. 흩어지는 어둠. 그리고 분노와 경악으로 일그러진 서천마군의 얼굴을.

강기가 깨져 나간 여파로 내상을 입은 놈의 입가에서 핏물과 고함이 쏟아져 내렸다.

“네놈이, 네놈이 감히-!”

“뭐, 씹새꺄.”

넌 이제…… 뒤졌어.

나는 환하게 웃으며 지면을 박찼다. 그리고 그런 나보다 한발 앞서 서천마군을 향해 쏘아지는 누군가의 신형이 있었다.

자그마한 체구. 잠시 흐트러졌던 기운을 수습한 적천강이었다.

- 무슨 일이 있었는지는 나중에 들으마.

짧은 전음이 뒤를 이었다.

- 우선 저 쌍노무 새끼부터 족치고.

좋아요를 누르고 싶어지는 댓글, 아니 전음이었다.



* * *



서천마군은 경악했다.

‘어찌, 어찌 이럴 수가 있단 말이냐!’

일백여 년의 세월. 수 갑자의 공력. 그가 지금까지 쌓아 올린 모든 것이 무너지고 있다. 부정당하고 있었다.

그것도 고작 이십 대에 불과한 핏덩이에게!

‘저런 게 가능하단 말인가?’

지금 이 순간, 서천마군의 뇌리를 스친 것은 의문을 넘어선 무언가였다.

‘괴력난신(怪力亂神).’

약관을 갓 넘긴 청년이 강기를 구현해 냈다. 그뿐인가, 거인의 힘과 바람의 빠르기를 지녔다.

실로 귀신의 도움이 아니고서야 설명할 수 없는 일이었다. 그러나……

‘죽는 것은 너희가 될 것이다.’

으득, 이를 악문 서천마군의 발이 땅에 닿았다. 그와 동시에 전신에서 강대한 기파가 넘실거리며 터져 나왔다.

“오너라!”

서천마군은 상처 입은 호랑이처럼 포효했다.

아니, 그는 실제로 상처 입은 호랑이가 맞았다. 오랜 전투로 누적된 피로와 소모된 공력. 한쪽 손목은 뽑혀 나갔고 발목은 부러졌다. 한순간의 오판으로 인해 핏덩이를 상대로 내상마저 입어야 했다.

그러나 그럼에도 변하지 않는 사실이 있었다.

“나는 천주의 충직한 종, 그분께서 함께하시는 한, 죽음마저 피해 가리라!”

장렬함마저 느껴지는 서천마군의 외침 뒤에, 늙고 젊은 두 개의 목소리가 따라붙었다.

“이놈이 지금 무슨 헛소리를 지껄이는 게냐?”

“암천이 아니라 암천지 같은데요. 야, 이만의 개새끼 해 봐.”

적천강과 진태경.

바람처럼 쇄도해 온 스승과 제자가 동시에 팔을 뻗었다.

꽈아앙!

굉음과 함께 가공할만한 기파가 휘몰아친 다음 순간, 한 사람의 입가에서 핏물이 흘러나왔다.

“쿨럭.”

엄청난 충격을 고스란히 받아 낸 서천마군의 신형이 작게 휘청였다.

평소였다면 모를까, 이미 심각한 부상을 입은 그에게 있어 두 초절정 고수의 합공은 실로 위협적이었다. 그러나 서천마군은 포기하지 않았다.

‘우선 한 놈부터 쓰러트린다.’

귀신의 도움을 받아 힘이 넘치는 젊은 제자와 부상의 여파에 시달리는 늙은 스승.

서천마군이 선택한 쪽은 당연하게도 후자였다.

“죽엇!”

서천마군의 다리가 채찍처럼 휘둘려졌다.

퍼엉!

무시무시한 파공성과 함께 날아든 발길질을 손으로 막아 낸 적천강이 침음성을 흘린 그 순간이었다.

“감히 누굴 건드려.”

뻐억! 으적!

번개처럼 턱을 올려친 창대에 눈앞이 번쩍인다. 호신강기로도 온전히 흡수하지 못한 엄청난 힘에 턱이 다물려지고 혓바닥이 잘려 나갔다.

고통과 충격을 느끼며 붕 떠오른 서천마군을 기다리는 것은 화염에 휩싸인 두 손이었다.

“노부가 화왕이다. 이 호로새끼야!”

적천강이 걸쭉한 욕설과 함께 화염신장을 내질렀다.

퍼벙!

안 그래도 위태롭던 호신강기가 흩어졌다. 극양의 열기는 어느새 거미줄처럼 금이 간 흑룡갑의 사이를 파고들었다.

불에 타는 듯한 통증과 함께 뜨거운 무언가가 목구멍을 타고 솟구쳤다.

“쿠웨에에엑!”

내장 조각이 섞인 검은 핏물이 뿜어졌다. 그리고 핏물이 바닥에 닿기도 전, 짧은 파공성이 서천마군의 귓가를 파고들었다.

쉬쉬쉬쉬쉭!

“……!”

실핏줄이 터져나간 서천마군의 붉은 눈동자에 비치는 수십 개의 창영(槍影).

허공을 종횡으로 태우며 날아드는 청백색 불꽃에 서천마군은 젖먹던 힘까지 끌어올렸다.

츠츠츠츠츠!

검신을 타고 솟구친 묵빛 검강이 창영과 부딪쳤다. 일격, 일격이 부딪칠 때마다 엄청난 굉음과 충격파가 지하 뇌옥을 뒤흔들고 서천마군의 내부마저 진탕시켰다.

“크허업……!”

그러나 그것으로 끝이 아니었다.

“한눈팔 겨를이 있느냐.”

서늘한 목소리가 들린 순간, 적천강의 멸염신권(滅炎神拳)이 서천마군의 옆구리를 파고들었다.

우직, 콰드드득!

십왕(十王) 중에서도 제일이라 불리는 화왕 적천강이 전력을 다해 펼친 일권이다.

막대한 충격을 견디지 못한 흑룡갑의 일부가 호신강기와 함께 깨져 나갔다. 살이 타고 뼈가 으스러졌다.

“크아아악!”

끔찍한 비명이 메아리처럼 울려 퍼졌다. 서천마군은 고통에 몸부림치면서도 남아 있는 모든 공력을 끌어 올려 사방에 퍼부었다.

쾅! 콰과과광!

지면, 천장, 기둥과 암석. 유형화된 묵빛 강기는 어느 것 하나 가리지 않고 쏘아졌다. 강기에 닿는 모든 것들이 가루가 되어 흩날리고 두부처럼 썰려 나갔다.

그러나 정작 목표가 되어야 할 두 사람은 강기의 그물을 찢고 서천마군의 앞에 도달해 있었다.

서걱!

투명한 창날에 맺힌 강기는 서천마군의 상반신을 비스듬히 갈랐고, 화염에 휩싸인 두 손바닥은 무너지려는 서천마군의 가슴을 후려쳤다.

퍼벙! 꽈앙!

“……!”

지금껏 경험해 본 적 없던, 아득한 고통과 함께 포탄처럼 튕겨 나간 서천마군의 신형이 단단한 암석을 부수고 벽면 깊숙이 처박혔다.

“끄억, 꺽.”

서천마군은 기괴한 신음과 함께 눈을 깜빡였다. 희미한 시야 속에서 걸어오는 두 사람이 보였다.

‘이렇게 죽는 것인가?’

서천마군은 멍하니 생각했다.

그는 오랜 세월 동안 강자로 군림했다. 약자를 짓밟고 그들의 소중한 것들을 빼앗으며 즐거워했다.

평범한 무림인은 누구나 한 번쯤 죽음을 생각하지만, 서천마군은 아니었다.

천하에 그의 목숨을 거둘 수 있는 것은 오직 자기 자신과 유일하며 존엄한 존재, 천주(天主)뿐이어야 했다.

그런데…….

“어찌하여 감히 네놈들 따위가 내 종을 죽이려 드느냐.”

피에 젖은 입술 사이로 사막의 모래알처럼 건조한 목소리가 흘러나왔다.

서천마군의 목소리에는 어떤 고통도, 이성도 느껴지지 않았다.

완전한 혈광(血光)을 띤 두 눈동자는 더 이상 인간의 것이 아니었고, 서천마군의 것도 아니었다.

“이 몸이 하늘로부터 지상에 임하니, 가장 아래에서부터 위까지 무릎을 꿇어라.”

그 순간, 적천강과 진태경이 벼락같은 외침을 토해 냈다.

“설마……!”

“천주!”

드드드득!

서천마군, 아니 잠시 서천마군의 몸을 빌린 그를 중심으로 뻗어 나간 가공할 기운이 땅과 천장을 뒤흔들었다.

뽑혀 나간 팔의 단면에서 묵색 기류가 촉수처럼 일렁이고, 폭포수 같은 피를 쏟아내는 상흔을 조금씩 메우고 있었다.

“나를 받들라. 전능한 권능 앞에 복속하라.”

투둑, 툭.

서천마군의 몸뚱어리가 천천히 몸을 일으켰다.

한 걸음, 한 걸음 다가오는 그의 등 뒤로 유형화된 공력이 날개처럼 펼쳐졌다.

그리고 다음 순간.

“……!”

모든 것이 정지했다. 진동도, 바람도, 흩날리던 먼지와 공기의 흐름조차도.

그렇게 모든 것이 정지된 세상 속에서, 한 줄기의 어둠이 쏘아졌다.

사아아아!

소리조차 없이 다가온 어둠이 두 사람을 집어삼킨다.

아니, 집어삼켰을 것이다.

찰나를 쪼개고 쪼갠 시간의 흐름을 가르고 뻗어 나온 창날이 아니었다면.

고오오오옹-

바람과 기운이 창날을 중심으로 응축되고, 이내 폭발하듯 터져 나왔다. 청백색 화염을 머금은 창날은 모든 것은 지우며 나아갔다.

일섬(一殲).

눈부신 섬광이 터져 나왔다.



* * *



멈췄던 시간이 다시 흐르며 찾아온 것은, 전신이 부서질 것 같은 통증과 탈력감이었다.

‘이대로 쓰러지고 싶다.’

팔과 다리, 손가락과 한 가닥의 근육까지. 내 신체를 이루고 있는 모든 것들이 금방이라도 끊어질 것 같다.

하지만 나는 초인적인 힘으로 버텼다.

아직은, 아직은 아니다. 적어도 놈보다 먼저 쓰러지고 싶지 않았다.

“그러니까 이제 좀 뒈져라, 시벌놈아.”

나는 고개를 들어 서천마군, 아니 서천마군의 몸뚱어리를 빌린 무언가를 바라보았다.

까맣게 타들어 간 전신과 뻥 뚫린 가슴을 확인한 놈의 입꼬리가 슬며시 위로 올라갔다.

“재미있군. 재미있어.”

푸스스.

말이 끝나기가 무섭게 재가 되어 흩날리는 손가락. 어디선가 불어온 한 줄기 바람에 놈의 몸이 천천히 허물어진다.

그러나 남의 몸을 빌린 놈은 고통을 느끼지 못한다. 오히려 웃음 섞인 한마디를 던졌다.

“다음에 또 보도록 하지.”

나는 간신히 중지를 치켜올렸다.

“좆이나 까 잡숴.”

대답은 돌아오지 않았다.

흩날리는 잿가루 너머, 퀘스트 성공과 레벨업을 알리는 시스템 알림이 울려 퍼진다.

그러나 싸움으로 인한 정신적인 피로는 회복되지 않았다.

그저 이대로 쓰러지고 싶었다. 아니, 이미 쓰러지는 중이다.

덥석.

그런 내 어깨를 붙든 것은 주름진 누군가의 손이었다.

화왕 적천강. 그의 반가운 얼굴을 마주하자, 문득 해야 할 말이 떠올랐다.

“어땠습니까?”

“뭐?”

“일섬. 끝내줬죠?”

걱정으로 가득하던 적천강의 얼굴이 스르륵 풀렸다. 이내 잔잔한 미소가 맺힌다.

“그래, 끝내줬다.”

그거면 됐습니다.

나는 새어 나오지 않는 대답과 함께 눈을 감았다. 지하 뇌옥이 무너지는 소리가 아련하게 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 365

*So this is what it feels like.*

The Supreme Peak realm. The domain of the great martial artists chosen by heaven.

I had taken a step into a place that had never been granted to me before, and I felt endless freedom.

How should I describe this feeling…

*This is incredible.*

A faint smile had already formed at the corners of my mouth.

Ding. Ding. Ding.

> **System**
>
> - The realm of **Fire Gate Divine Technique** has advanced to the eighth stage.
> - The realm of **Fire Dragon Divine Spear** has advanced to the eighth stage!
> - **Flamefire Path** has advanced to…!

System notifications announcing increases in various martial arts, along with Level Ups and achievement completions, rang out without pause.

Qi like molten lava surged from deep within my entire body. The darkness rushing toward Jeok Cheongang and me no longer frightened me in the slightest.

“Die!”

A scream-like shout. A face twisted like a fiend.

There was no trace left of the middle-aged man who had once worn a good-natured smile.

Only a monster consumed by killing intent remained.

Whoooosh!

The ink-black Sword Force, wrapped in savage killing intent, came crashing down like a bolt of lightning. I could feel the destructive power lurking within it just by looking at it.

But…

*In the end, you were human too.*

The Western Heaven Demon Lord was already exhausted from his injuries and fatigue, and his excessive rage had scattered his mind.

When the mind wavered, so did the qi. You could not pierce a boulder with a needle, but passing between grains of sand was not difficult.

Sss.

One step. As the tip of my foot pushed against the ground, space vanished.

Jeok Cheongang hurriedly shouted when he saw my back suddenly blocking his path.

“You little bastard, get back—”

His voice could not continue. Cyan-white energy was surging over the transparent spearhead of White Flame.

Filled with the heat of Extreme Yang, the energy connected toward itself like tangled threads, gathered together, and finally took shape.

A beautiful yet destructive concentration of internal energy. The exclusive province of great martial artists.

*Force.*

I had finally made it this far.

Trembling with joy, I thrust my arm toward the darkness rushing at me.

Ssssh!

A single line was drawn through the air. Cyan-white flames shot forward like an arrow and collided with the darkness.

Heavenly Strike.

The fire dragon's claws tore the ink-colored Force to pieces.

KRAAAAAA!

Amid the deafening roar, I could see it clearly. The scattering darkness. And the Western Heaven Demon Lord's face, twisted with rage and shock.

Blood and a howl poured from his mouth as the backlash of his shattered Force inflicted an Internal Injury.

“You dare—you dare!”

“What, you fucking bastard?”

*You’re fucking dead now.*

I smiled brightly and kicked off the ground. But someone had already shot toward the Western Heaven Demon Lord, one step ahead of me.

A small body. Jeok Cheongang, who had gathered the qi that had briefly fallen out of balance.

—I'll hear what happened later.

A short Sound Transmission followed.

—First, let's beat down that double-damned bastard.

It was the kind of comment that made me want to hit the Like button—or rather, it was a Sound Transmission.

* * *

The Western Heaven Demon Lord was stunned.

*How? How could this be happening?*

More than a hundred years of time. Several jiazi of internal energy. Everything he had built up until now was collapsing. Being denied.

And by a mere brat in his twenties!

*Could such a thing be possible?*

At this moment, the thought that flashed through the Western Heaven Demon Lord's mind went beyond doubt.

*Supernatural powers.*

A young man barely past twenty had manifested Force. And that was not all. He possessed the strength of a giant and the speed of the wind.

It was something that could not be explained without the aid of a ghost. And yet…

*You will be the ones who die.*

The Western Heaven Demon Lord clenched his teeth and planted his foot on the ground. At the same time, a powerful qi aura surged from his entire body and burst outward.

“Come!”

The Western Heaven Demon Lord roared like an injured tiger.

No—he really was an injured tiger. Fatigue accumulated through a long battle and exhausted internal energy. One wrist had been torn away, and one ankle had been broken. Because of a momentary misjudgment, he had even suffered an Internal Injury at the hands of a mere brat.

But even so, one fact remained unchanged.

“I am the Lord of Heaven’s loyal servant. So long as that person is with me, even death itself shall pass me by!”

The Western Heaven Demon Lord’s shout carried an almost heroic grandeur. Two voices—one old, one young—immediately followed.

“What kind of bullshit are you spouting now?”

“Sounds less like Dark Heaven and more like Darkcheonji.[^1] Hey, try saying, ‘Lee Man-ui is a son of a bitch.’”

[^1]: “Darkcheonji” and “Lee Man-ui” parody Shincheonji and its founder, Lee Man-hee; challenging a presumed follower to insult its leader is the joke.

Jeok Cheongang and Jin Taekyung.

Master and Disciple rushed forward like the wind and thrust out their arms at the same time.

KWAANG!

After a terrifying qi aura swept through the underground prison with a thunderous roar, blood began to flow from one man's mouth.

“Cough.”

The Western Heaven Demon Lord's body staggered slightly after absorbing the tremendous impact head-on.

Under normal circumstances, perhaps it would have been different. But for a man who had already suffered serious injuries, the joint attack of two Supreme Peak masters was truly threatening.

Even so, the Western Heaven Demon Lord did not give up.

*I’ll bring down one of them first.*

A young Disciple overflowing with strength thanks to the aid of a ghost, and an old Master suffering from the effects of his injuries.

Naturally, the Western Heaven Demon Lord chose the latter.

“Die!”

His leg swung like a whip.

Boom!

At the moment Jeok Cheongang blocked the terrifying kick with his hand and let out a low groan—

“How dare you touch him.”

Crack! Crunch!

The spear shaft struck upward like lightning and caught the Western Heaven Demon Lord beneath the jaw. His vision flashed white. The tremendous force, which even his Body-Protecting Qi could not fully absorb, snapped his jaw shut and severed his tongue.

The Western Heaven Demon Lord rose into the air from the pain and impact. Waiting for him were two hands wreathed in flame.

“This old man is the Fire King, you fucking bastard!”

Jeok Cheongang unleashed the Flame Divine Palm along with a thick curse.

BOOM!

The already unstable Body-Protecting Qi scattered. The heat of Extreme Yang seeped between the cracks in the Black Dragon Armor, which had split like a spiderweb.

Along with a pain like being burned alive, something hot surged up his throat.

“Gwaaaaaaagh!”

Black blood mixed with pieces of his organs sprayed out. Before the blood could even reach the ground, a brief sound of something cutting through the air pierced the Western Heaven Demon Lord's ears.

Ssssh-sh-sh-sh!

“……!”

Dozens of spear shadows appeared in the Western Heaven Demon Lord's bloodshot eyes, with burst blood vessels spreading across them.

As cyan-white flames flew through the air, scorching it in every direction, the Western Heaven Demon Lord dragged up every last bit of strength he possessed.

Ssssss!

Ink-colored Sword Force surged along his blade and collided with the spear shadows. Every clash produced a tremendous roar and shock wave that shook the underground prison and churned the Western Heaven Demon Lord's insides.

“Graaagh…!”

But it was not over.

“Do you have time to look away?”

At the sound of the cold voice, Jeok Cheongang's Flame-Extinguishing Divine Fist drove into the Western Heaven Demon Lord's side.

Crack! KRRRUNCH!

This was a punch unleashed with all the strength of Jeok Cheongang, the Fire King who was called the greatest among the Ten Kings.

Part of the Black Dragon Armor shattered along with the Body-Protecting Qi, unable to withstand the enormous impact. Flesh burned, and bones broke.

“Gaaaaah!”

A horrific scream reverberated. Even as he writhed in agony, the Western Heaven Demon Lord drew up every bit of his remaining internal energy and unleashed it in all directions.

BOOM! KWA-KWAKWANG!

The ground, ceiling, pillars, and rocks. The manifested ink-colored Force shot out without discrimination. Everything it touched turned to dust or was sliced apart like tofu.

Yet the two people who should have been its targets had already torn through the net of Force and reached the Western Heaven Demon Lord.

Shhk!

The Force gathered on the transparent spearhead slashed diagonally through the Western Heaven Demon Lord's upper body, while the two flame-wreathed palms struck his collapsing chest.

BOOM! KWAANG!

“……!”

The Western Heaven Demon Lord's body was hurled away like a cannonball, accompanied by an unimaginable pain he had never experienced before. It smashed through solid rock and buried itself deep in the wall.

“Ghk, ghek.”

The Western Heaven Demon Lord blinked with a bizarre groan. Through his blurred vision, he saw two people walking toward him.

*Is this how I die?*

The Western Heaven Demon Lord thought blankly.

For a long time, he had reigned as a powerful figure. He had enjoyed trampling the weak and taking away the things they cherished.

Every ordinary martial artist in Murim thought about death at least once. But not the Western Heaven Demon Lord.

The only beings in the world who should have been capable of taking his life were himself and the one sole, dignified existence known as the Lord of Heaven.

And yet…

“How dare you wretches try to kill my servant?”

A dry voice, like grains of sand in a desert, slipped between his blood-soaked lips.

There was no pain or reason in the Western Heaven Demon Lord's voice.

His two eyes, shining with pure bloodlight, were no longer human.

Nor did they belong to the Western Heaven Demon Lord anymore.

“As this body descends to earth from heaven, kneel—from the lowest to the highest.”

At that moment, Jeok Cheongang and Jin Taekyung shouted like thunder.

“No way…”

“The Lord of Heaven!”

Rumble-rumble!

A terrifying energy spread from the Western Heaven Demon Lord—or rather, from the being temporarily borrowing his body—and shook the ground and ceiling.

An ink-colored current writhed like a tentacle from the stump of his torn-off arm, slowly sealing the wound that had been gushing blood like a waterfall.

“Worship me. Submit before omnipotent power.”

Plop. Plop.

The Western Heaven Demon Lord's body slowly rose.

With every step he took toward them, manifested internal energy spread out behind him like wings.

And then—

“……!”

Everything stopped. The trembling, the wind, even the drifting dust and the movement of the air.

In that world where everything had stopped, a streak of darkness shot forward.

Ssssss!

The darkness approached without a sound and swallowed them both.

No—it would have, if not for the spearhead that thrust out, cleaving through a flow of time divided into ever-finer instants.

Gooooooong—

Wind and qi condensed around the spearhead, then burst out like an explosion. The spearhead, carrying cyan-white flames, advanced while erasing everything in its path.

One Annihilation.

A blinding flash erupted.

* * *

When time began to flow again, it brought with it pain that made my entire body feel as though it were breaking apart, along with complete exhaustion.

*I want to collapse just like this.*

My arms and legs, my fingers, even every individual strand of muscle. Every part of my body felt as though it might snap at any moment.

But I held on with superhuman strength.

*Not yet. Not yet.*

At the very least, I did not want to collapse before him.

“So die already, you fucking bastard.”

I raised my head and looked at the Western Heaven Demon Lord—or rather, the thing borrowing the Western Heaven Demon Lord's body.

After confirming that his entire body had been burned black and that a hole had been blown through his chest, the corners of his mouth slowly lifted.

“Interesting. Very interesting.”

Fwoosh.

No sooner had he finished speaking than his fingers turned to ash and scattered. In a breeze that had come from somewhere, his body slowly began to crumble.

But the thing borrowing another person's body could not feel pain. Instead, it tossed out a single line with a laugh.

“We’ll meet again next time.”

I barely raised my middle finger.

“Go eat a dick.”

No answer came.

Beyond the drifting ash, System notifications announcing Quest success and Level Up rang out.

But the mental fatigue caused by the battle did not recover.

I only wanted to collapse right there. No—I was already in the process of collapsing.

Grab.

A wrinkled hand caught my shoulder.

It belonged to Jeok Cheongang, the Fire King. When I saw his welcome face, I suddenly remembered something I needed to say.

“How was it?”

“What?”

“One Annihilation. It was incredible, right?”

The concern filling Jeok Cheongang's face slowly faded. Before long, a gentle smile formed on his lips.

“Yes. It was incredible.”

That was enough.

Alongside an answer that never escaped my lips, I closed my eyes. The sound of the underground prison collapsing echoed faintly in the distance.
```
